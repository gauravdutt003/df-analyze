from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from random import randint, uniform
from typing import TYPE_CHECKING, Optional, cast

import jsonpickle
import numpy as np
from pandas import DataFrame, Series

if TYPE_CHECKING:
    from src.cli.cli import ProgramOptions
from src.enumerables import ClsScore, RegScore, WrapperSelection, WrapperSelectionModel
from src.preprocessing.prepare import PreparedData
from src.selection.stepwise import stepwise_select
from src.testing.datasets import TestDataset


@dataclass
class WrapperSelected:
    method: WrapperSelection
    model: WrapperSelectionModel
    selected: list[str]
    scores: dict[str, float]
    is_classification: bool

    def to_markdown(self) -> str:
        fnames, scores = zip(*self.scores.items())
        scores = DataFrame(
            data=scores, index=Series(name="feature", data=fnames), columns=["score"]
        )
        metric = ClsScore.Accuracy if self.is_classification else RegScore.MAE
        mname = metric.longname()
        higher_better = self.is_classification
        direction = "Higher" if higher_better else "Lower"
        text = (
            "# Wrapper-Based Feature Selection Summary\n\n"
            f"Wrapper method: {self.method.name}\n"
            f"Wrapper model:  {self.model.name}\n"
            "\n"
            f"## Selected Features\n\n"
            f"{self.selected}\n\n"
            f"## Selection Scores ({mname}: {direction} = More important)\n\n"
            f"{scores.to_markdown(floatfmt='0.3e')}"
        )
        return text

    @staticmethod
    def from_json(path: Path) -> WrapperSelected:
        return cast(WrapperSelected, jsonpickle.decode(path.read_text()))

    def to_json(self) -> str:
        return str(jsonpickle.encode(self))

    @staticmethod
    def random(ds: TestDataset) -> WrapperSelected:
        method = WrapperSelection.random()
        model = WrapperSelectionModel.random()
        df = ds.load()
        x = df.drop(columns="target", errors="ignore")
        cols = x.columns.to_list()
        n_feat = randint(min(10, x.shape[1]), x.shape[1])
        selected = np.random.choice(cols, size=n_feat, replace=False).tolist()
        scores = {s: uniform(0, 1) for s in selected}
        return WrapperSelected(
            method=method,
            model=model,
            selected=selected,
            scores=scores,
            is_classification=ds.is_classification,
        )


def wrap_select_features(
    prep_train: PreparedData, options: ProgramOptions
) -> Optional[WrapperSelected]:
    if options.wrapper_select is None:
        return None

    result = stepwise_select(prep_train=prep_train, options=options)
    if result is None:
        return None
    selected, scores = result

    return WrapperSelected(
        selected=selected,
        scores=scores,
        method=options.wrapper_select,
        model=options.wrapper_model,
        is_classification=prep_train.is_classification,
    )