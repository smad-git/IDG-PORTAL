import { PropsWithChildren } from 'react';
import { ChildrenProps } from '../../types/CommonTypes';

export const Header: React.FC<PropsWithChildren<ChildrenProps>> = () => {
  return (
    <>
      <header className="header">
        <h1>Header</h1>
      </header>
    </>
  );
};
