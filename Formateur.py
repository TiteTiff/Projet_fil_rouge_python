from Utilisateur import Utilisateur


class Formateur (Utilisateur):
	def __init__(self, nom:str, id:int):
		super().__init__(nom, id)

	def peut_valider(self, competence_id: int) -> bool:
		return True