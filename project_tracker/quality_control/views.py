from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from .forms import BugReportForm, FeatureRequestForm

from .models import BugReport, FeatureRequest
from django.views import View


def index(request):
    return render(request, 'quality_control/index.html')


#     link_bugs = reverse('page_bugs')
#     link_features = reverse('page_features')
#     html_response = f'''
#     <h1>Система контроля качества</h1>
#     <a href = {link_bugs}>Список всех багов</a>
#     <br>
#     <a href = {link_features}>Запросы на улучшение</a>
#     '''
#     return HttpResponse(html_response)


def bug_list(request):
    all_bugs = BugReport.objects.all()
    return render(request, 'quality_control/bug_list.html', {
        'all_bugs': all_bugs
    })

    # all_bugs = BugReport.objects.all()
    # html_response = '<h1>Cписок отчетов об ошибках</h1><ul>'
    # for bug in all_bugs:
    #     html_response += f'<li><a href="{bug.id}">{bug.title}</a> со статусом - {bug.status}</li>'
    # html_response += '</ul>'
    # return HttpResponse(html_response)


def bug_detail(request, bug_id):
    get_bug = get_object_or_404(BugReport, id=bug_id)
    return render(request, 'quality_control/bug_detail.html', {
        'get_bug': get_bug
    })


#     get_bug = get_object_or_404(BugReport, id=bug_id)
#     to_bug = reverse('projects_list')
#     link_to_bug = f'{to_bug}{get_bug.project.id}'
#     html_response = f'''<h1>Детали бага {get_bug.title}</h1>
#     <p>Описание: {get_bug.description}</p>
#     <p>Статус: {get_bug.status}</p>
#     <p>Приоритет: {get_bug.priority}</p>
#     <p>Проект, в котором найден баг: <a href = {link_to_bug}>{get_bug.project.name}</a></p>
#     <p>Задача, в которой найден баг:<a href = {link_to_bug}/tasks/{get_bug.task.id}>{get_bug.task.name}</a></p>
#     '''
#     return HttpResponse(html_response)


def feature_list(request):
    all_feature_requests = FeatureRequest.objects.all()
    return render(request, 'quality_control/feature_list.html', {
        'all_feature_requests': all_feature_requests
    })

    # all_feature_requests = FeatureRequest.objects.all()
    # html_response = '<h1>Список запросов на улучшение</h1>'
    # for feature_request in all_feature_requests:
    #     html_response += f'<li><a href="{feature_request.id}">{feature_request.title}</a> со статусом - {feature_request.status}</li>'
    # html_response += '</ul>'
    # return HttpResponse(html_response)


def feature_id_detail(request, feature_id):
    get_feature = get_object_or_404(FeatureRequest, id=feature_id)
    return render(request, 'quality_control/feature_id_detail.html', {
        'get_feature': get_feature
    })


#     get_feature = get_object_or_404(BugReport, id=feature_id)
#     to_project = reverse('projects_list')
#     link_to_project = f'{to_project}{get_feature.project.id}'
#     html_response = f'''<h1>Детали задачи {get_feature.title}</h1>
#         <p>Описание: {get_feature.description}</p>
#         <p>Статус: {get_feature.status}</p>
#         <p>Приоритет: {get_feature.priority}</p>
#         <p>Проект, в котором нужно сделать доработку: <a href = {link_to_project}>{get_feature.project.name}</a></p>
#         <p>Задача, в которой нужно сделать доработку: <a href = {link_to_project}/tasks/{get_feature.task.id}>{get_feature.task.name}</a></p>
#         '''
#     return HttpResponse(html_response)


# class IndexView(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'quality_control/index.html')

#     def get(self, request, *args, **kwargs):
#         link_bugs = reverse('page_bugs')
#         link_features = reverse('page_features')
#         html_response = f'''
#             <h1>Система контроля качества</h1>
#             <a href = {link_bugs}>Список всех багов</a>
#             <br>
#             <a href = {link_features}>Запросы на улучшение</a>
#         '''
#         return HttpResponse(html_response)


# class BugDetailView(DetailView):
#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#     template_name = 'quality_control/bug_detail.html'

#     model = BugReport
#     pk_url_kwarg = 'bug_id'
#
# def get(self, request, *args, **kwargs):
#     get_bug = self.get_object()
#         to_bug = reverse('projects_list')
#         link_to_bug = f'{to_bug}{get_bug.project.id}'
#         html_response = f'''<h1>Детали бага {get_bug.title}</h1>
#             <p>Описание: {get_bug.description}</p>
#             <p>Статус: {get_bug.status}</p>
#             <p>Приоритет: {get_bug.priority}</p>
#             <p>Проект, в котором найден баг: <a href = {link_to_bug}>{get_bug.project.name}</a></p>
#             <p>Задача, в которой найден баг:<a href = {link_to_bug}/tasks/{get_bug.task.id}>{get_bug.task.name}</a></p>
#             '''
#         return HttpResponse(html_response)


# class FeatureIdDetailView(DetailView):
#     model = FeatureRequest
#     pk_url_kwarg = 'feature_id'
#     template_name = 'quality_control/feature_id_detail.html'
#
#     def get(self, request, *args, **kwargs):
#         get_feature = self.get_object()
#         to_project = reverse('projects_list')
#         link_to_project = f'{to_project}{get_feature.project.id}'
#         html_response = f'''<h1>Детали задачи {get_feature.title}</h1>
#             <p>Описание: {get_feature.description}</p>
#             <p>Статус: {get_feature.status}</p>
#             <p>Приоритет: {get_feature.priority}</p>
#             <p>Проект, в котором нужно сделать доработку: <a href = {link_to_project}>{get_feature.project.name}</a></p>
#             <p>Задача, в которой нужно сделать доработку: <a href = {link_to_project}/tasks/{get_feature.task.id}>{get_feature.task.name}</a></p>
#             '''
#         return HttpResponse(html_response)


def create_bugreport(request):
    if request.method == 'POST':
        form = BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_bugs')
    else:
        form = BugReportForm()
    return render(request, 'quality_control/bug_report_form.html', {'form': form})


def create_feature(request):
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('page_features')
    else:
        form = FeatureRequestForm()
    return render(request, 'quality_control/feature_request_form.html', {'form': form})


class BugReportCreateView(CreateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bug_report_form.html'
    success_url = reverse_lazy('page_bugs')


class FeatureCreateView(CreateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_request_form.html'
    success_url = reverse_lazy('page_features')


def update_bugreport(request, bug_id):
    bug = get_object_or_404(BugReport, pk=bug_id)
    if request.method == 'POST':
        form = BugReportForm(request.POST, instance=bug)
        if form.is_valid():
            form.save()
            return redirect('page_bug_detail', bug_id=bug.id)
    else:
        form = BugReportForm(instance=bug)
    return render(request, 'quality_control/bugreport_update.html', {'form': form, 'bug': bug})


def update_feature(request, feature_id):
    feature = get_object_or_404(FeatureRequest, pk=feature_id)
    if request.method == 'POST':
        form = FeatureRequestForm(request.POST, instance=feature)
        if form.is_valid():
            form.save()
            return redirect('page_feature_detail', feature_id=feature.id)
    else:
        form = FeatureRequestForm(instance=feature)
    return render(request, 'quality_control/feature_update.html', {'form': form, 'feature': feature})


#
class BugReportUpdateView(UpdateView):
    model = BugReport
    form_class = BugReportForm
    template_name = 'quality_control/bugreport_update.html'
    pk_url_kwarg = 'bug_id'

    def get_success_url(self):
        return reverse_lazy('page_bug_detail',
                            kwargs={'bug_id': self.object.id})


class FeatureUpdateView(UpdateView):
    model = FeatureRequest
    form_class = FeatureRequestForm
    template_name = 'quality_control/feature_update.html'
    pk_url_kwarg = 'feature_id'

    def get_success_url(self):
        return reverse_lazy('page_feature_detail',
                            kwargs={'feature_id': self.object.id})


# def delete_bugreport(request, bug_id):
#     bug = get_object_or_404(BugReport, pk=bug_id)
#     bug.delete()
#     return redirect('page_bugs')
#
#
# def delete_feature(request, feature_id):
#     feature = get_object_or_404(FeatureRequest, pk=feature_id)
#     feature.delete()
#     return redirect('page_features')


class BugReportDeleteView(DeleteView):
    model = BugReport
    pk_url_kwarg = 'bug_id'
    success_url = reverse_lazy('page_bugs')
    template_name = 'quality_control/bugreport_confirm_delete.html'

    # def get_success_url(self):
    #     return reverse_lazy('page_bug_detail', kwargs={'bug_id': self.object.id})


class FeatureDeleteView(DeleteView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'
    success_url = reverse_lazy('page_features')
    template_name = 'quality_control/feature_confirm_delete.html'
