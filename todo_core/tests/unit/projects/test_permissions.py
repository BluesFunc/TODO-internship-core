import pytest
from projects.permission import (
    IsProjectCollaboratorPermission,
    IsProjectCreatorPermission,
    IsProjectEditorPermission,
)
from rest_framework.request import Request

permission_test_invalid_data = {
    "argnames": ["user_data", "project_id"],
    "argvalues": [
        [{}, "12345"],
        [{"YOLO": "42"}, "1333333"],
        [{"user_id": "52"}, "ZZZXXXasd"],
        [{"user_id": ""}, "0060152d-cb6e-49c2-8ea1-0a7883df7952"],
        [{"user_id": "0060152d-cb6e-49c2-8ea1-0a7883df7952"}, ""],
        [
            {"user_id": "f1fbebd4-f515-4b20-ab86-0d4c3b679715"},
            "ef877f41-3bed-4e51-86e3-590cb1aab01c",
        ],
    ],
}


@pytest.mark.parametrize(**permission_test_invalid_data)
@pytest.mark.django_db
def test_colaborator_permission(
    mock_request_authorized_user, mock_project_viewset, user_data, project_id
):
    permission = IsProjectCollaboratorPermission()
    request = mock_request_authorized_user(user_data)
    viewset = mock_project_viewset(project_id)

    has_permission = permission.has_permission(
        mock_request_authorized_user, mock_project_viewset
    )
    assert has_permission is False


@pytest.mark.parametrize(**permission_test_invalid_data)
@pytest.mark.django_db
def test_project_creator_permission(
    mock_request_authorized_user, mock_project_viewset, user_data, project_id
):
    permission = IsProjectCreatorPermission()
    request = mock_request_authorized_user(user_data)
    viewset = mock_project_viewset(project_id)
    has_permission = permission.has_permission(mock_request_authorized_user, viewset)
    assert has_permission is False


@pytest.mark.parametrize(**permission_test_invalid_data)
@pytest.mark.django_db
def test_project_editor_permission(
    mock_request_authorized_user, mock_project_viewset, user_data, project_id
):
    permission = IsProjectEditorPermission()
    request = mock_request_authorized_user(user_data)
    viewset = mock_project_viewset(project_id)
    has_permission = permission.has_permission(request, viewset)
    assert has_permission is False
