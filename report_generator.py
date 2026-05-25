class ReportGenerator:

    def generate(self, results):

        report = "\n===== FINAL CASE REPORT =====\n"

        for r in results:

            report += f"\nSuspect: {r['name']}\n"
            report += f"Suspicion Score: {r['score']}\n"

            report += "Reasons:\n"

            for reason in r["reasons"]:
                report += f"- {reason}\n"

        return report