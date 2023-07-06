import { Grid } from '@mui/material';
import Dashboard from './Dashboard';
import SignIn from './Components/signin';
import SignUp from './Components/signup';
import { createTheme, ThemeProvider } from '@mui/material/styles';
//ABEBFF, 80CAE0
const theme = createTheme({
  palette: {
    background: {
      default: "#136C87"
    },
    text: {
      primary: "#E0B78D",
      secondary: "#946537"
    },
    primary: {
      main: '#E0B78D'
    },
    secondary: {
      main: '#946537'
    }
  }
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <SignIn></SignIn>
    </ThemeProvider>
  );
}

export default App;