import json

from abc import ABC, abstractmethod

class BaseAction(ABC):

    @classmethod
    def from_op(cls, op_data):
        """A factory method to instantiate an Action object from a blockchain
        operation data.

        :param op_data (dict): Operation data
        :return (Action): Action instance
        """
        if op_data.get("id") != cls.CUSTOM_JSON_ID:
            raise ValueError("Invalid Custom JSON ID.")

        json_metadata = json.loads(op_data["json"])
        constructor = [json_metadata.get(p) for p in cls.PROPERTIES]
        return cls(*constructor)

    def to_transaction(self):
        """Prepares a valid blockchain operation object from the instance.

        Every subclass is responsible to implement _generate_json method.
        """
        return {
                "from": self.account,
                "id": self.CUSTOM_JSON_ID,
                "json": self._generate_json(),
                "required_auths": [],
                "required_posting_auths": [self.account],
        }

    @abstractmethod
    def _generate_json(self):
        raise NotImplementedError
