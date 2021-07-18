import { render, screen } from '@testing-library/react';
import App from './App';

test('renders', () => {
  render(<App />);
  const linkElement = screen.getByText(/traffic incidents/i);
  expect(linkElement).toBeInTheDocument();
});
