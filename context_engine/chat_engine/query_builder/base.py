from abc import ABC, abstractmethod
from typing import List

from context_engine.chat_engine.models import HistoryPruningMethod
from context_engine.models.data_models import Messages, Query


class QueryBuilder(ABC):

    @abstractmethod
    def build(self,
              messages: Messages,
              max_prompt_tokens: int,
              *,
              history_pruning: HistoryPruningMethod
              ) -> List[Query]:
        pass

    async def abuild(self,
                     messages: Messages,
                     max_prompt_tokens: int,
                     history_pruning: HistoryPruningMethod
                     ) -> List[Query]:
        raise NotImplementedError
