from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect ,get_object_or_404
from todo.models import TodoModel
from todo.forms import TodoForm
from django.views import generic


class CreateTodoView(generic.CreateView):
    template_name = 'todo/cteate_todo.html'
    form_class = TodoForm
    success_url = '/todo_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateTodoView, self).form_valid(form=form)




# def create_todo_view(request):
#     if request.method == 'POST':
#         form = TodoForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('todoList')
        

    # else:
    #     form=TodoForm()
    #     return render(request, template_name='todo/create_todo.html', context={'form' : form})
        



class TodoListView(generic.ListView):
    template_name = 'todo/todo_list.html'
    context_object_name = 'todo_List'
    model = TodoModel

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')
# def todo_list_view(request):
#     if request.method == 'GET':
#         todo_list = TodoModel.objects.all().order_by(-id)
#         context = {
#             'todo_list' : todo_list
#         }
#         return render(request, template_name='todo/todo_list.html', context=context)
    





class TodoDetailView(generic.DetailView):
    template_name = 'todo/todo_detail.html'
    context_object_name = 'todo_id'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(TodoModel, id=todo_id)
# def todo_detail_view(request, id):
#     if request.method == 'GET':
#         todo_id = get_object_or_404(TodoModel, id=id)
#         context = {'todo_id' : todo_id}
#         return render(
#             request,
#             template_name='todo/todo_detail.html'
#             context=context
#             )
    


class UpdateTodoView(generic.UbdateTodo):
    template_todo = 'todo/todo_update.html'
    form_class = TodoForm
    success_url = '/todo_list/'

    def form_valid (self, form):
        print(form.cleaned_data)
        return super(UpdateTodoView, self).form_valid(form=form)
    
    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('-id')
        return get_object_or_404(TodoModel, id=todo_id)
        
#def update_todo_view(request, id):
#     todo_id = get_object_or_404(TodoModel, id=id)
#     if request.method == 'POST':
#         form = TodoForm(request.POST, instance=todo_id)
#         if form.is_valid():
#             form.save()
#             return redirect('todoList')
#     else:
#         form = TodoForm(instance=todo_id)
#         return render(request, 
#                       template_name='todo/todo-update.html', 
#                       context={
#                           "todo_id" : todo_id,
#                           "form" : form
#                       }
#                       )
    

class DeleteTodoView(generic.DeleteView):
    template_name = 'todo/confirm_delete.html'
    success_url = '/todo_list/'

    def get_object(self, **kwargs):
        todo_id = self.kwargs.get('id')
        return get_object_or_404(TodoModel, id=todo_id)
    


# def delete_todo_view(request, id):
#     todo_id = get_object_or_404(TodoModel, id=id)
#     todo_id.delete()
#     return redirect('todoList')

