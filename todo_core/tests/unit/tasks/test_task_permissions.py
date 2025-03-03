from typing import Type

import pytest
from pytest_lazy_fixtures import lf
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import Project, ProjectCollaborators
from tasks.models import Task
from tasks.permissions import (
    IsCreateAndEditTasksPermission,
    IsGetTaskPermission,
    IsHaveTaskAccess,
)


@pytest.mark.parametrize(
    "permission_class,user_request,expected_result",
    [
        (
            IsGetTaskPermission,
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            IsGetTaskPermission,
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
        (
            IsHaveTaskAccess,
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            IsHaveTaskAccess,
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
        (
            IsCreateAndEditTasksPermission,
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            IsCreateAndEditTasksPermission,
            lf("mock_request_user_without_permissions"),
            False,
        ),
        (
            IsCreateAndEditTasksPermission,
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
    ],
)
@pytest.mark.django_db
def test_task_permissions(
    mock_project_nested_viewset: APIView,
    user_request: Request,
    permission_class: Type[BasePermission],
    expected_result: bool,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
    task_instance: Task,
) -> None:
    permission = permission_class()
    permission_result = permission.has_permission(
        request=user_request, view=mock_project_nested_viewset
    )

    permission_obj_result = permission.has_object_permission(
        request=user_request, view=mock_project_nested_viewset, obj=task_instance
    )
    result = permission_result and permission_obj_result
    assert result is expected_result
