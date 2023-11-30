from src.dao.general_dao import GeneralDAO
from src.domain.cluster_program import ClusterProgram


class ClusterProgramDao(GeneralDAO):
    _domain_type = ClusterProgram

    def get_subjects_in_cluster_program(self, cluster_program_id):
        try:

            cluster_program = self.find_by_id(cluster_program_id)

            if not cluster_program:
                return None

            subjects_in_cluster_program = cluster_program.subjects

            result = []

            for subject in subjects_in_cluster_program:
                result.append({
                    "subject_id": subject.id,
                    "subject_name": subject.name,
                    "subject_description": subject.description,
                })

            return result

        except Exception as e:
            print(f"Error: {e}")
            return None
