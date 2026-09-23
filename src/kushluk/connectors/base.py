from __future__ import annotations

from typing import Protocol

from kushluk.models import Candidate, PracticalItem


class CandidateConnector(Protocol):
    def fetch(self) -> list[Candidate]: ...


class PracticalConnector(Protocol):
    def fetch(self) -> list[PracticalItem]: ...
