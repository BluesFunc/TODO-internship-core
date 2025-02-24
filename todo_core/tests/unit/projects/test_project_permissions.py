import pytest
from projects.models import Project, ProjectCollaborators
from projects.permissions import (
    IsCreateProjectPermission,
    IsProjectCreatorPermission,
    IsProjectViewerPermission,
    IsReadProjects,
)
from pytest_lazy_fixtures import lf
from rest_framework.request import Request
from rest_framework.views import APIView


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_project_create_permission(
    mock_project_viewset: APIView,
    permissioned_user: Request,
    create_project_permission: IsCreateProjectPermission,
) -> None:
    positive_permission_test = create_project_permission.has_permission(
        permissioned_user, mock_project_viewset
    )

    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_permissions")]
)
@pytest.mark.django_db
def test_negative_project_create_permission(
    mock_project_viewset: APIView,
    create_project_permission: IsCreateProjectPermission,
    permissionless_user: Request,
) -> None:
    permission = IsCreateProjectPermission()

    negative_permission_test = permission.has_permission(
        permissionless_user, mock_project_viewset
    )

    assert negative_permission_test is False


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_project_get_permission(
    mock_project_viewset: APIView,
    permissioned_user: Request,
    project_reader_permission: IsReadProjects,
) -> None:
    positive_permission_test = project_reader_permission.has_permission(
        permissioned_user, mock_project_viewset
    )

    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_permissions")]
)
@pytest.mark.django_db
def test_negative_project_get_permission(
    mock_project_viewset: APIView,
    project_reader_permission: IsReadProjects,
    permissionless_user: Request,
) -> None:
    negative_permission_test = project_reader_permission.has_permission(
        permissionless_user, mock_project_viewset
    )

    assert negative_permission_test is False


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_project_editor_permission(
    mock_project_viewset: APIView,
    permissioned_user: Request,
    project_creator_permission: IsProjectCreatorPermission,
    project_instance: Project,
) -> None:

    positive_permission_test = project_creator_permission.has_object_permission(
        permissioned_user, mock_project_viewset, project_instance
    )

    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_permissions")]
)
@pytest.mark.django_db
def test_negative_project_editor_permission(
    mock_project_viewset: APIView,
    permissionless_user: Request,
    project_creator_permission: IsProjectCreatorPermission,
    project_instance: Project,
) -> None:

    negative_permission_test = project_creator_permission.has_object_permission(
        permissionless_user, mock_project_viewset, project_instance
    )

    assert negative_permission_test is False


@pytest.mark.parametrize(
    "permissioned_user",
    [lf("mock_request_full_permission_user")],
)
@pytest.mark.django_db
def test_positive_project_viewer_permission(
    mock_project_viewset: APIView,
    permissioned_user: Request,
    project_viewer_permission: IsProjectViewerPermission,
    project_instance: Project,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    positive_permission_test = project_viewer_permission.has_permission(
        permissioned_user, mock_project_viewset
    )

    assert positive_permission_test is True


@pytest.mark.parametrize(
    "permissionless_user", [lf("mock_request_user_without_permissions")]
)
@pytest.mark.django_db
def test_negative_project_viewer_permission(
    mock_project_viewset: APIView,
    permissionless_user: Request,
    project_instance: Project,
    project_viewer_permission: IsProjectViewerPermission,
    project_collaborator_editor_instance: ProjectCollaborators,
) -> None:

    negative_permission_test = project_viewer_permission.has_permission(
        permissionless_user,
        mock_project_viewset,
    )

    assert negative_permission_test is False
