from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

def pg_records(request,queryset_list,num):
	paginator = Paginator(queryset_list, num)
	page = request.GET.get('page')
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		#if page is not an integer, deliver the first page.
		queryset = paginator.page(1)
	except EmptyPage:
		#if page is out of range(e.g.9999), deliver the last page of results.
		queryset = paginator.page(paginator.num_pages)
	return queryset