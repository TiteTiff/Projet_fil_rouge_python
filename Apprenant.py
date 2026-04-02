from Utilisateur import Utilisateur


class Apprenant(Utilisateur):
	def __init__(self, nom:str, id:int, competences_validees:list[int | str]):
		super().__init__(nom, id)
		self._competences_validees = competences_validees

	def peut_valider(self, competence_id: int) -> bool:
		if competence_id in self._competences_validees:
			return True
		else:
			return False

	def ajouter_competence(self, competence_id:int)->None:
		if competence_id in self._competences_validees:
			raise ValueError("Cette valeur est un double")
		else:
			self._competences_validees.append(competence_id)


