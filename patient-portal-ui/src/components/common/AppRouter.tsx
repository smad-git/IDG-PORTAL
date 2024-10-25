import { Route, Routes } from 'react-router-dom';
import { MainLandingPage } from '../main/MainLandingPage';
import { useMemo } from 'react';

interface Routes {
  path: string;
  component: JSX.Element;
  children: Routes[];
}

export const ROUTES: Routes[] = [
  {
    path: '/',
    component: <MainLandingPage />,
    children: [],
  },
];

export const AppRouter: React.FC = (props) => {
  const getComponent = (component: JSX.Element, path: string) => {
    return component;
  };

  const renderRoutesRecursive = (routes: Routes[]) => {
    return routes.map((route, index) => {
      if (route.children) {
        return (
          <Route
            key={index}
            path={route.path}
            element={getComponent(route.component, route.path)}
          >
            {renderRoutesRecursive(route.children)}
          </Route>
        );
      } else {
        return (
          <Route
            key={index}
            path={route.path}
            element={getComponent(route.component, route.path)}
          />
        );
      }
    });
  };

  const renderRoutes = useMemo(() => renderRoutesRecursive(ROUTES), [ROUTES]);

  return (
    <>
      <Routes>{renderRoutes}</Routes>
    </>
  );
};
