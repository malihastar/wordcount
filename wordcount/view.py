from django.http import HttpResponse
from django.shortcuts import render
import  operator
def home(request):
      return render(request,'Home.html')
def about(request):
      return render(request,'about.html')
def count(request):
      fulltex=request.GET['fulltext']
      textlist=fulltex.split()
      worddictionary={}
      for word in textlist:
            if word in worddictionary:
                  worddictionary[word] += 1
            else:
                  worddictionary[word] = 1
            sordword=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)




      return  render(request,'count.html', {'fulltext':fulltex, 'counttext':len(textlist), 'worddictionary':sordword})



