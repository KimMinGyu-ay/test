from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect, render
from .models import user_list





def home(request):
    return HttpResponse("Home!")
    
def register(request):
    if request.method == "GET":
        return render(request, "register/register.html")
    elif request.method == "POST":
        username = request.POST['username']
        age = request.POST['age']
        gender = request.POST['gender']
        ID = request.POST['ID']
        pw = request.POST['password']
        email = request.POST['email']
        # if pw != re_pw:
        #     return HttpResponse("")
        user_infor =user_list(
            user_name = username,
            gender = gender,
            age = age,
            user_id = ID,
            password =pw,
            e_mail =email
        )
        user_infor.save()
        return render(request, "register/register.html")


def login(request):
    if request.method=="GET":
        return render(request, "register/login.html")
    elif request.method=="POST":
        userId =request.POST.get("userid")  # get("HTML에 name설정한거")
        password =request.POST.get("password")
    res_data={}
    if  not(userId and password):
        res_data['error']='모든 값을 입력하세요'
    else:
        user = user_list.objects.get(user_id=userId)
        print(password, user.password)
        if password == user.password:
            request.session['user'] = user.user_id
            return redirect("/main")
        else:
            res_data['error'] = "비밀번호가 틀렸습니다."
        return render(request, 'register/login.html',res_data)

    
    
    return render(request,"register/login.html")
# # User 탈퇴 1
# def delete(request):
#     user = request.user
#     user.delete()
#     logout(request)
#     return render(request, "update/update.html")

# User 탈퇴 2
# def delete(request,id):
#     if request.method == 'POST':
#         user =get_object_or_404(user_list, pk=id)
#         user.delete()
#         return redirect('/user')
#     return render(request, 'update/update.html')

def mypage(request,id):
    try:
        user = user_list.objects.get(pk=id)
    except user_list.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'update/mypage.html', {'user': user})


def delete(request,id):
    user =get_object_or_404(user_list, pk=id)
    user.delete()
    return redirect('/main') # 탈퇴가 완료 됐습니다 문구 후 로그인창으로 돌아오게


# # User 정보 수정
# 로그인 된 상태에서 실행
def user_update(request,id):
    user =get_object_or_404(user_list, pk=id)
    if request.method == 'POST':
        user.password = request.POST['password']
        user_list( password=user.password).save()
        return redirect('/main')
    else:
        return render(request,'update/update.html',{'user':user})


# def update(request):
#     if request.method == 'POST':
#         user_change_from = CustomUserChangeForm(request.POST, instance=request.user)
#         if user_change_form.is_valid():
#             user_change_form.save()
#             return redirect('accounts:people', request.user.username)
    
#     else:
#         user_change_form = CustomUserChangeForm(instance = request.user)
#         return render(request, 'accounts/update.html', {
#                                     'user_change_form':user_change_form})



