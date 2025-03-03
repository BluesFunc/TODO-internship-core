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
            lf("project_creator_permission"),
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            lf("project_creator_permission"),
            lf("mock_request_user_without_test_project_access"),
            False,
        ),
        (
            lf("create_project_permission"),
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            lf("create_project_permission"),
            lf("mock_request_user_without_permissions"),
            False,
        ),
        (
            lf("project_reader_permission"),
            lf("mock_request_full_permission_user"),
            True,
        ),
        (
            lf("project_reader_permission"),
            lf("mock_request_user_without_permissions"),
            False,
        ),
    ],
)
@pytest.mark.django_db
def test_project_logic_permission(
    mock_project_viewset: APIView,
    user_request: Request,
    permission: BasePermission,
    expected_result: bool,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:
    permission_result = permission.has_permission(
        request=user_request, view=mock_project_viewset
    )

    permission_obj_result = permission.has_object_permission(
        request=user_request, view=mock_project_viewset, obj=project_instance
    )
    result = permission_result and permission_obj_result
    assert result is expected_result
