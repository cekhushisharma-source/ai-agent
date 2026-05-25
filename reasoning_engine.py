class ReasoningEngine:

    def analyze(self, text):

        suspects = ["John", "Mike", "Sarah"]

        results = []

        for suspect in suspects:

            score = 0
            reasons = []

            if suspect.lower() in text.lower():

                score += 30
                reasons.append(
                    f"{suspect} mentioned in case file"
                )

            if "fingerprint" in text.lower():

                score += 40
                reasons.append(
                    "Fingerprint evidence detected"
                )

            if "cctv" in text.lower():

                score += 20
                reasons.append(
                    "CCTV evidence detected"
                )

            results.append({
                "name": suspect,
                "score": score,
                "reasons": reasons
            })

        results = sorted(
            results,
            key=lambda x: x["score"],
            reverse=True
        )

        return results