import { PropsWithChildren } from 'react';
import { ChildrenProps } from '../../types/CommonTypes';

export const Footer: React.FC<PropsWithChildren<ChildrenProps>> = () => {
  return (
    <>
      <footer className="footer">
        <p>Footer</p>
      </footer>
    </>
  );
};
