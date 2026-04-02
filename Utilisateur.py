class Utilisateur:
	def __init__(self, nom:str, id:int):
		self.nom=nom
		self.id=id

	def peut_valider(self, competence_id:int) ->bool:
		return False

	def __str__(self)->str:
		return f"Utilisateur : {self.nom}, id : {self.id}"


