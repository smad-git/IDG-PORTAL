import { PropsWithChildren } from 'react';
import { ChildrenProps } from '../../types/CommonTypes';
import { Header } from './Header';
import { Footer } from './Footer';
import { PatientPortalSearch } from '../patient-portal/PatientPortalSearch';
import { Box } from '@mui/material';

export const MainLandingPage: React.FC<
  PropsWithChildren<ChildrenProps>
> = () => {
  return (
    <>
      <Box className="app-container">
        <Header />
        <div className="body-content">
          <PatientPortalSearch />
        </div>
        <Footer />
      </Box>
    </>
  );
};
