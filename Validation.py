from dataclasses import dataclass


@dataclass
class Validation:
	id:int
	apprenant_id:int
	competence_id:int
	statut:str
	pre_valide_par:str

