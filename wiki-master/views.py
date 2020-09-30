from django.shortcuts import render,redirect
import markdown as md
import random
from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries()
    })

def title(request, title):
    if util.get_entry(title):
        content = util.get_entry(title)
        return render(request,'encyclopedia/content.html',{
            'title': title,
            'content': md.markdown(content)
        })
    else:
        return render(request,'encyclopedia/error.html',{
            'title':title
        })

def search(request):
    query = request.POST.get('q')
    # print(query)
    if util.get_entry(query):
        return redirect('title', title = query)
    else:
        all_entry = list(util.list_entries())
        matched = [s for s in all_entry if query.lower() in s.lower()]
        if len(matched) != 0:
            return render(request, 'encyclopedia/searchpage.html', {
                'entries':matched
            })
        else:
            return render(request,'encyclopedia/error.html')

def create(request):
    print('hello')
    return  render(request,'encyclopedia/create_page.html')

def save(requst):
    title = requst.POST.get('title')
    markdown = requst.POST.get('markdown')

    if util.get_entry(title):
        return render(requst,'encyclopedia/pageexists.html',{
            'title':title
        })
    else:
        util.save_entry(title,markdown)
        return redirect('title',title=title)

def editpage(request,title):
    print('hi')
    print(util.get_entry(title))
    return render(request,'encyclopedia/editpage.html',{
        'title': title,
        'markdown': util.get_entry(title)
    })

def editted_saved(request,title):
    # print('1')
    markdown = request.POST.get('markdown')

    print(markdown)
    title = title
    # print('3')
    util.save_entry(title,markdown)
    # print('5')
    return redirect('title',title=title)

def random_page(request):
    entries = list(util.list_entries())
    title = random.choice(entries)
    return redirect('title',title=title)









