import { render, screen } from '@testing-library/react';
import Incidents from './Incidents';

test('renders', () => {
    render(<Incidents />);
    const linkElement = screen.getByText(/traffic incidents/i);
    expect(linkElement).toBeInTheDocument();
});
