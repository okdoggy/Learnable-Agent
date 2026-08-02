from __future__ import annotations

import json
from pathlib import Path

from lala.api.app import create_app
from lala.config import Settings
from lala.domain.models import EditPlan
from lala.knowledge.models import RawScenario, TechnicalNoteSubmission
from lala.renderers.inspection import ImageInspection
from lala.text import write_utf8_lf

ROOT = Path(__file__).resolve().parents[1]


class DocumentationPlanner:
    def plan(
        self,
        *,
        request_id: str,
        prompt: str,
        image_path: Path,
        inspection: ImageInspection,
    ) -> EditPlan:
        del request_id, prompt, image_path, inspection
        raise RuntimeError("documentation-only planner")


def write_json(path: Path, value: object) -> None:
    write_utf8_lf(
        path,
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
    )


def main() -> None:
    write_json(ROOT / "schemas" / "edit-plan.schema.json", EditPlan.model_json_schema())
    write_json(ROOT / "schemas" / "raw-scenario.schema.json", RawScenario.model_json_schema())
    write_json(
        ROOT / "schemas" / "technical-note.schema.json",
        TechnicalNoteSubmission.model_json_schema(),
    )
    temporary_settings = Settings.from_env(ROOT)
    app = create_app(temporary_settings, planner=DocumentationPlanner())
    write_json(ROOT / "schemas" / "openapi.json", app.openapi())


if __name__ == "__main__":
    main()
