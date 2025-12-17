import React from 'react';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

const TableOfContents = [
  {
    id: 'ch-001',
    title: 'Introduction to Robotics and Automation',
    link: 'docs/CHAPTERS/chapter-01',
  },
  {
    id: 'ch-002',
    title: 'Mechanical Aspects of Robotics',
    link: 'docs/CHAPTERS/chapter-02',
  },
  {
    id: 'ch-003',
    title: 'Designing the AI-Robot Communication Bridge',
    link: 'docs/CHAPTERS/chapter-03',
  },
  {
    id: 'ch-004',
    title: 'The AI Core: Perception, Planning, and Action',
    link: 'docs/CHAPTERS/chapter-04',
  },
  {
    id: 'ch-005',
    title: 'The Authoritative Source Mandate',
    link: 'docs/CHAPTERS/chapter-05',
  },
  {
    id: 'ch-006',
    title: 'The Human as Tool Strategy',
    link: 'docs/CHAPTERS/chapter-06',
  },
  {
    id: 'ch-007',
    title: 'Project Governance and Evolution',
    link: 'docs/CHAPTERS/chapter-07',
  },
  {
    id: 'ch-008',
    title: 'The Role of Specifications in SDD',
    link:'docs/CHAPTERS/chapter-08',
  },
  {
    id: 'ch-009',
    title: 'Practical Guide to Prompt History Records (PHR)',
    link: 'docs/CHAPTERS/chapter-09',
  },
  {
    id: 'ch-010',
    title: 'Architectural Decision Records (ADRs) in Practice',
    link: 'docs/CHAPTERS/chapter-10',
  },
  {
    id: 'ch-011',
    title: 'Ensuring Quality with Small, Testable Changes',
    link: 'docs/CHAPTERS/chapter-11',
  },
  {
    id: 'ch-012',
    title: "The Agent's Execution Contract",
    link: 'docs/CHAPTERS/chapter-12',
  },
  {
    id: 'ch-013',
    title: 'Putting It All Together: A Case Study',
    link: 'docs/CHAPTERS/chapter-13',
  },
];

function TOCItem({ id, title, link }) {
  return (
    <Link to={link} className={styles.tocCard}>
      <span className={styles.chapterId}>{id}</span>
      <h3>{title}</h3>
    </Link>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.tocSection}>
      <div className="container">
        <h2 className={styles.tocTitle}>📘 Table of Contents</h2>

        <div className={styles.tocGrid}>
          {TableOfContents.map((item, idx) => (
            <TOCItem key={idx} {...item} />
          ))}
        </div>
      </div>
    </section>
  );
}
