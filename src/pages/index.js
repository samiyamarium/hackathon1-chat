import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <h1 className="toctitle">
          Physical AI and Humanoid Robotics
        </h1>

        <p className="hero__subtitle">
          A practical guide to intelligent agents, robotics architecture,
          and human–AI collaboration
        </p>

        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="docs/CHAPTERS/chapter-01">
            📖 Start Reading
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title="Physical AI and Humanoid Robotics"
      description="An in-depth book on Physical AI, humanoid robotics, intelligent agents, and real-world system design">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
      </main>
    </Layout>
  );
}
