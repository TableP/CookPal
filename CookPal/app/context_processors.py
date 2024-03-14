from .models import UserAccount, User  # Import your UserAccount model

def useraccount(request):
    # Add the useraccount model to the context
    useraccount = None
    if request.user.is_authenticated:
        useraccount = UserAccount.objects.get(user=request.user)

    return {'useraccount': useraccount}