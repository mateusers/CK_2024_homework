from django.db import models
# from tasks.models import Project, Task
import tasks.models


class BugReport(models.Model):
    status_bug = [
        ('NEW', "Новая"),
        ('IN_WORK', "В работе"),
        ('COMPLETED', "Завершена")
    ]

    priority_bug = [
        ('ZERO', '0'),
        ('ONE', '1'),
        ('TWO', '2'),
        ('THREE', '3'),
        ('FOUR', '4'),
        ('FIVE', '5')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        tasks.models.Project,
        related_name='bug_reports',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        tasks.models.Task,
        related_name='bug_reports',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=30,
        choices=status_bug,
        default='NEW'
    )
    priority = models.CharField(
        max_length=5,
        choices=priority_bug,
        default='NULL'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class FeatureRequest(models.Model):
    status_request = [
        ('CONSIDERATION', "Рассмотрение"),
        ('ACCEPTED', "Принято"),
        ('REJECTED', "Отклонено")
    ]

    priority_request = [
        ('ZERO', '0'),
        ('ONE', '1'),
        ('TWO', '2'),
        ('THREE', '3'),
        ('FOUR', '4'),
        ('FIVE', '5')
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(
        tasks.models.Project,
        related_name='feature_requests',
        on_delete=models.CASCADE
    )
    task = models.ForeignKey(
        tasks.models.Task,
        related_name='feature_requests',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    status = models.CharField(
        max_length=30,
        choices=status_request,
        default='CONSIDERATION'
    )
    priority = models.CharField(
        max_length=5,
        choices=priority_request,
        default='NULL'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)