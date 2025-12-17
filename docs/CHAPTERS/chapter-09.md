# Chapter 9: Practical Guide to Prompt History Records (PHR)

## Introduction

In the evolving paradigm of AI-assisted software development, transparency, traceability, and accountability are paramount. The Humanoid Robot project, built on the principles of Spec-Driven Development (SDD), introduces a cornerstone mechanism to achieve these objectives: the Prompt History Record (PHR). PHRs are not merely logs; they are meticulously crafted, immutable documents that capture every significant interaction between the user and the agent, along with crucial details of the agent's actions and decisions. This chapter provides a practical guide to understanding, implementing, and utilizing PHRs, highlighting their indispensable role as a complete audit trail for the development process.

The rationale behind PHRs stems from the need to demystify AI agents' operations. While agents can perform complex tasks, their internal reasoning processes often remain opaque. By diligently recording prompts, responses, and the context surrounding each interaction, PHRs offer a window into the agent's decision-making, enabling effective debugging, continuous learning, and robust compliance verification. This chapter will dissect the anatomy of a PHR, outlining its essential components and their significance. Subsequently, we will explore the practical aspects of implementing and leveraging PHRs within the project workflow, emphasizing both automated and manual creation processes, and underscoring the manifold benefits they bring to AI-driven development.

## Section 1: The Anatomy of a PHR

A Prompt History Record is a structured Markdown file, typically with a YAML front-matter, designed to encapsulate all pertinent information about a specific agent-user interaction. Each field serves a distinct purpose, contributing to the comprehensive nature of the record.

### Essential Fields and Their Significance

1.  **`id`**: A unique, sequential identifier (e.g., `0001`). This ensures that every PHR can be uniquely referenced and that the historical sequence of interactions is preserved.

2.  **`title`**: A concise, human-readable summary of the interaction (3–7 words), which also forms the slug for the filename. This allows for quick identification of the PHR's content.

3.  **`stage`**: Categorizes the interaction based on its phase in the development lifecycle (e.g., `constitution`, `spec`, `plan`, `tasks`, `red`, `green`, `refactor`, `explainer`, `misc`, `general`). This provides crucial context for later analysis and routing.

4.  **`date`**: The date of the interaction in ISO format (YYYY-MM-DD). Essential for chronological tracking and historical analysis.

5.  **`surface`**: Indicates the interface or platform through which the interaction occurred (e.g., `agent`, `cli`, `chat`). This helps in understanding the operational environment.

6.  **`model`**: Identifies the specific AI model used for the interaction (e.g., `gemini`, `gpt-4`). Critical for tracking model performance and debugging model-specific issues.

7.  **`feature`**: If the interaction is feature-specific, this field holds the feature name or identifier. Useful for organizing PHRs by feature, especially in large projects.

8.  **`branch`**: The Git branch where the interaction took place. Provides context for code changes and version control.

9.  **`user`**: Identifies the human user interacting with the agent. Enables tracking interactions back to specific individuals.

10. **`command`**: The exact command or initial prompt that initiated the interaction. This is the starting point for understanding the agent's response.

11. **`labels`**: A list of tags or keywords (e.g., `["bug-fix", "refactoring"]`) for categorization and filtering. Enhances discoverability and analysis.

12. **`links`**: Structured links to related artifacts like specifications, tickets, ADRs, or Pull Requests. Establishes a web of interconnected documentation.

13. **`files`**: A YAML list of files created or modified during the interaction, including their paths. Provides a direct record of code changes.

14. **`tests`**: A YAML list of tests run or added during the interaction. Crucial for verifying the impact of changes.

### Core Elements: Prompt and Response

Beyond the front-matter, the body of a PHR captures the essence of the interaction:

*   **`PROMPT_TEXT`**: The user's input, captured verbatim and unedited. This ensures a faithful record of the request the agent received, allowing for retrospective analysis of clarity and intent.
*   **`RESPONSE_TEXT`**: A concise but representative summary of the agent's key output or action. This provides a quick overview of what the agent did in response to the prompt.

Together, these fields and the prompt/response body create a complete, self-contained narrative of each development step, making the AI-assisted process transparent and auditable.

## Section 2: Implementing and Utilizing PHRs

The effective implementation and utilization of PHRs are crucial for harnessing their full potential in AI-assisted development. This involves a clear process for their creation and a strategic understanding of their benefits.

### The PHR Creation Process

The constitution outlines a detailed process for PHR creation, designed to ensure consistency and completeness:

1.  **Detect Stage**: The agent first determines the stage of the interaction (e.g., `spec`, `plan`, `misc`). This dictates the routing and context of the PHR.
2.  **Generate Title and Routing**: A concise title is generated, and based on the stage, the PHR is routed to the appropriate subdirectory (e.g., `history/prompts/constitution/`, `history/prompts/<feature-name>/`, or `history/prompts/general/`).
3.  **Automated Creation (Preferred)**: Ideally, a dedicated script (e.g., `create-phr.sh`) handles the automated creation, filling in as many placeholders as possible. This minimizes manual effort and ensures adherence to the template.
4.  **Manual Fallback**: If automation fails or is unavailable, the agent falls back to a manual process:
    *   Read the PHR template.
    *   Allocate a new, incremented ID.
    *   Compute the output path.
    *   Fill all placeholders, including verbatim `PROMPT_TEXT` and concise `RESPONSE_TEXT`.
5.  **Validation**: Post-creation, the PHR undergoes validation to ensure no placeholders remain, title/stage/dates are consistent, and the `PROMPT_TEXT` is complete.

### Benefits of Utilizing PHRs

PHRs offer significant advantages for both human developers and the project itself:

*   **Debugging and Root Cause Analysis**: By tracing the sequence of prompts and responses, developers can quickly identify when and how a particular issue was introduced, making debugging much more efficient.
*   **Knowledge Transfer**: PHRs serve as an invaluable knowledge base, allowing new team members (human or AI) to quickly understand the project's history, decisions, and evolution without needing to piece together scattered information.
*   **Transparency and Auditability**: Every agent action is explicitly recorded, providing complete transparency into the development process. This is crucial for regulatory compliance and internal audits.
*   **Learning and Improvement**: Analyzing PHRs can reveal patterns in agent behavior, identify common failure modes, and provide insights for improving agent performance, prompt engineering, and overall development workflows.
*   **Compliance Verification**: In the context of SDD, PHRs can be used to verify that agents are adhering to the project's constitutional principles, such as ensuring that every significant action is logged.

## Conclusion

Prompt History Records are more than just a historical archive; they are an active and indispensable tool for effective AI-assisted software development within the Humanoid Robot project. By meticulously documenting every user-agent interaction and agent action, PHRs create a transparent, traceable, and auditable narrative of the project's evolution. They empower developers to debug more efficiently, facilitate knowledge transfer, ensure compliance with project governance, and provide a rich dataset for continuous improvement of AI agents. In an era where AI is becoming an integral part of the development lifecycle, the disciplined practice of PHR creation stands as a beacon of clarity and accountability, ensuring that every step taken is understood, verifiable, and contributes to the project's success.
