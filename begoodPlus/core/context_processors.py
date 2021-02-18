

from .forms import FormBeseContactInformation
def loadBaseInfo(request):
    contactForm = FormBeseContactInformation()
    context  = {'contactForm': contactForm}
    return context