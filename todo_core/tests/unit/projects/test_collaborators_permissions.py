import pytest
from pytest_lazy_fixtures import lf
from rest_framework.permissions import BasePermission
from rest_framework.request import Request
from rest_framework.views import APIView

from projects.models import Project, ProjectCollaborators


@pytest.mark.parametrize(
    "permission,user_request,expected_result",
    [
        (
            lf("project_collaborator_reader_permission"),
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            lf("project_collaborator_reader_permission"),
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
        (
            lf("project_collaborator_editor_permission"),
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            lf("project_collaborator_editor_permission"),
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
    ],
)
@pytest.mark.django_db
def test_collaborator_permissions(
    mock_project_nested_viewset: APIView,
    user_request: Request,
    expected_result: bool,
    permission: BasePermission,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    permission_result = permission.has_permission(
        request=user_request, view=mock_project_nested_viewset
    )
    assert permission_result is expected_result
