from typing import Type
from uuid import UUID, uuid4

import pytest
from pytest_lazy_fixtures import lf

from projects.models import Project
from projects.services import ProjectService


@pytest.mark.parametrize(
    "project_id,expected_value",
    [
        (
            lf("project_instance.id"),
            lf("project_instance"),
        ),
        (uuid4(), None),
    ],
)
@pytest.mark.django_db
def test_get_by_id(
    project_service_class: Type[ProjectService],
    project_id: UUID,
    expected_value: Project | None,
) -> None:
    result = project_service_class.get_by_id(project_id)
    assert result == expected_value
