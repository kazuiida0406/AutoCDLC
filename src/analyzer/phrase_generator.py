from model.phrase import Phrase
from model.phrase_iteration import PhraseIteration



class PhraseGenerator:
    """
    Rocksmith Phrase Generator

    Phrase定義と配置を分離
    """



    def __init__(self):

        pass



    # ==========================================
    # Generate Phrases
    # ==========================================

    def generate(
        self,
        arrangement
    ):

        phrases = []


        # 基本フレーズ生成

        phrases.append(

            Phrase(

                id=0,

                name="main_riff",

                max_level_difficulty=3

            )

        )


        return phrases



    # ==========================================
    # Generate Iterations
    # ==========================================

    def generate_iterations(
        self,
        arrangement
    ):


        iterations = []


        for phrase in arrangement.phrases:


            iterations.append(

                PhraseIteration(

                    phrase_id=phrase.id,

                    time=0.0

                )

            )


        return iterations