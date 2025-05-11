# https://github.com/anthropics/anthropic-cookbook/blob/main/patterns/agents/basic_workflows.ipynb
# Example 2: Parallelization workflow for stakeholder impact analysis
# Process impact analysis for multiple stakeholder groups concurrently

from concurrent.futures import ThreadPoolExecutor
from typing import List
from utils import llm_call


def parallel(prompt: str, inputs: List[str], n_workers: int = 3) -> List[str]:
    """Process multiple inputs concurrently with the same prompt."""
    with ThreadPoolExecutor(max_workers=n_workers) as executor:
        futures = [executor.submit(llm_call, f"{prompt}\nInput: {x}") for x in inputs]
        return [f.result() for f in futures]

stakeholders = [
    """Customers:
    - Price sensitive
    - Want better tech
    - Environmental concerns""",
    
    """Employees:
    - Job security worries
    - Need new skills
    - Want clear direction""",
    
    """Investors:
    - Expect growth
    - Want cost control
    - Risk concerns""",
    
    """Suppliers:
    - Capacity constraints
    - Price pressures
    - Tech transitions"""
]

impact_results = parallel(
    """Analyze how market changes will impact this stakeholder group.
    Provide specific impacts and recommended actions.
    Format with clear sections and priorities.""",
    stakeholders
)

for result in impact_results:
    print(result)