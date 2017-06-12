
from django.core.paginator import Paginator

def paginate_queryset(objs,page_no,cnt_per_age=3,half_show_length=3):
    p = Paginator(objs,cnt_per_age)
    if page_no > p.num_pages:
        page_no = p.num_pages
    if page_no <= 0:
        page_no = 1
    page_links = [i for i in range(page_no - half_show_length,page_no + half_show_length + 1)
                  if i > 0 and i<=p.num_pages ]
    page = p.page(page_no)
    page_first = page_links[0] - 1
    page_max = page_links[-1] + 1
    #print("p.page_links...............:",p.count)
    paginate_data = {"has_previous":page_first > 0,
                     "has_next":page_max <= p.num_pages,
                     "page_first":page_first ,
                     "page_links":page_links,
                     "page_max":page_max,
                     "page_no":page_no,
                     "page_links":page_links,
                     "page_next":page_no + 1,
                     "page_pre":page_no - 1,
                     "count":p.count}
    #print("paginate_data............................................:",paginate_data)
    return (page.object_list,paginate_data)




