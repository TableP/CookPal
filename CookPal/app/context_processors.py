from .models import UserAccount, User  # Import your UserAccount model

def useraccount(request):
    # Add the useraccount model to the context
    useraccount = None
    if request.user.is_authenticated:
        try:
            useraccount = UserAccount.objects.get(user=request.user)
        except UserAccount.DoesNotExist:
            useraccount = None

    return {'useraccount': useraccount}