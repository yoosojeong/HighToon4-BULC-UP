from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models
from .forms import LoginForm
from .forms import SignupForm
from .forms import PostingDataForm

class Home(APIView):
    def get(self, request, format=None):

        return render(request, "home.html", {})

class Profile(APIView):     
    def get(self, request, format=None):
        
        return render(request, "profile.html", {})
        
class Signup(APIView):
    
    def post(self, request, format=None):
        
        form = SignupForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            
            SignupForm(request.FILES['profile_image'])
        
        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):

        form = SignupForm()

        return render(request, "signup_form.html", {'form': form})

class List(APIView):
    def get(self, request, format=None):
        postingDatas = models.PostingData.objects.all()
        context = { 'postingDatas' : postingDatas }

        return render(request, "list.html", context)

class Posting(APIView):
            
    def post(self, request, format=None):

        user = request.user

        form = PostingDataForm(user, request.POST)

        if form.is_valid():
            form.save()

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request, format=None):

        user = request.user

        form = PostingDataForm(user)

        return render(request, "posting.html", {'form': form})

class PostDetail(APIView):

    def find_post(self, post_id):
        
        try:
            postBox = models.PostingData.objects.get(id=post_id)
            return postBox

        except models.PostingData.DoesNotExist:
            return None
    
        except models.Profile.DoesNotExist:
            return None

    def find_own_post(self, post_id, user):
   
        creator = models.Profile.objects.get(name=user)

        try:
            postBox = models.PostingData.objects.filter(id=post_id, creator=creator)
            return postBox

        except models.PostingData.DoesNotExist:
            return None

        except models.Profile.DoesNotExist:
            return None

    def get(self, request, post_id, format=None):
        #포스트 보기

        postBox = self.find_post(post_id)
       
        context = { 'postBox' : postBox }

        return render(request, "postDetail.html", context)
    
    def put(self, request, post_id, format=None):
        #포스트 올리기

        user = request.user

        postBox = self.find_own_post(post_id, user)

        if postBox is None:

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        if request.data == None:
    
             return Response(status=status.HTTP_401_UNAUTHORIZED)

        postBox.update(**request.data)

        return Response(status=status.HTTP_204_NO_CONTENT)       

    def delete(self, request, post_id, format=None):

        user = request.user 

        postBox = self.find_own_post(post_id, user)

        if postBox is None:

            return Response(status=status.HTTP_401_UNAUTHORIZED)
    
        postBox.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ChangePassword(APIView):

    def put(self, request, username, format=None):

        user = request.user

        if user.username == username:

            current_password = request.data.get('current_password', None) #없으면 none
            
            if current_password is not None:

                password_match = user.check_password(current_password) #현재 비번이 맞는 지 체크

                if password_match:
                    
                    new_password = request.data.get('new_password', None)

                    if new_password is not None:

                        user.set_password(new_password)

                        user.save()

                        return Response(status=status.HTTP_200_OK)
                    
                    else:
                        
                        return Response(status=status.HTTP_400_BAD_REQUEST)
                else:
                    
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            
            return Response(status=status.HTTP_400_BAD_REQUEST)
