

import logo from './logo.svg';


function App() {
  return (
    <Router>
      <div className="container py-4">
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary rounded mb-4">
          <NavLink className="navbar-brand fw-bold d-flex align-items-center" to="/">
            <img src={logo} alt="Octofit Logo" className="me-2" style={{ height: '40px', width: '40px' }} />
            Octofit Tracker
          </NavLink>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav">
              <li className="nav-item"><NavLink className="nav-link" to="/activities">Activities</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/leaderboard">Leaderboard</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/teams">Teams</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/users">Users</NavLink></li>
              <li className="nav-item"><NavLink className="nav-link" to="/workouts">Workouts</NavLink></li>
            </ul>
          </div>
        </nav>
        <div className="row justify-content-center">
          <div className="col-12 col-lg-10">
            <Routes>
              <Route path="/activities" element={<Activities />} />
              <Route path="/leaderboard" element={<Leaderboard />} />
              <Route path="/teams" element={<Teams />} />
              <Route path="/users" element={<Users />} />
              <Route path="/workouts" element={<Workouts />} />
              <Route path="/" element={<div className="text-center mt-5"><h1 className="display-4 mb-3">Welcome to <span className="text-primary">Octofit Tracker</span>!</h1><p className="lead">Track your fitness, join teams, and compete on the leaderboard.</p></div>} />
            </Routes>
          </div>
        </div>
      </div>
    </Router>
  );
}

export default App;
