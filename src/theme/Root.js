import React from 'react';
import ChatbotComponent from '@theme/ChatbotComponent';

// Default implementation, that you can customize
export default function Root({children}) {
  return (
    <>
      {children}
      <ChatbotComponent />
    </>
  );
}
