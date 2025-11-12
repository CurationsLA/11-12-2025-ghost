// CurationsLA Add-Ons - Sports Live Data JavaScript
// Fetches real-time sports data for web-only integration

/**
 * Initialize Sports Live Data functionality
 * @param {string} containerId - ID of the container element
 */
function initSportsLiveData(containerId) {
  const container = document.getElementById(containerId);
  if (!container) {
    console.log('Sports container not found:', containerId);
    return;
  }

  // Load sports data from various sources
  loadSportsData(container);
  
  // Refresh data every 5 minutes
  setInterval(() => {
    loadSportsData(container);
  }, 5 * 60 * 1000);
}

/**
 * Load and display sports data
 * @param {HTMLElement} container - Container element
 */
async function loadSportsData(container) {
  const scoresGrid = container.querySelector('#live-scores-grid');
  if (!scoresGrid) return;

  try {
    // Show loading state
    scoresGrid.innerHTML = '<div class="score-item loading">Loading live scores...</div>';

    // Fetch sports data from multiple sources
    const sportsData = await fetchSportsData();
    
    if (sportsData && sportsData.length > 0) {
      displaySportsData(scoresGrid, sportsData);
    } else {
      displayNoData(scoresGrid);
    }
  } catch (error) {
    console.error('Error loading sports data:', error);
    displayError(scoresGrid);
  }
}

/**
 * Fetch sports data from APIs
 * @returns {Promise<Array>} Sports data array
 */
async function fetchSportsData() {
  const endpoints = [
    fetchLATeamsData(),
    fetchMLBScores(),
    fetchNBAScores(),
    fetchNFLScores()
  ];

  try {
    const results = await Promise.allSettled(endpoints);
    const validResults = results
      .filter(result => result.status === 'fulfilled')
      .map(result => result.value)
      .flat()
      .filter(Boolean);

    return validResults;
  } catch (error) {
    console.error('Error fetching sports data:', error);
    return [];
  }
}

/**
 * Fetch LA-specific teams data
 * @returns {Promise<Array>} LA teams data
 */
async function fetchLATeamsData() {
  const laTeams = [
    { team: 'Lakers', league: 'NBA', api: 'nba' },
    { team: 'Clippers', league: 'NBA', api: 'nba' },
    { team: 'Dodgers', league: 'MLB', api: 'mlb' },
    { team: 'Angels', league: 'MLB', api: 'mlb' },
    { team: 'Rams', league: 'NFL', api: 'nfl' },
    { team: 'Chargers', league: 'NFL', api: 'nfl' },
    { team: 'LAFC', league: 'MLS', api: 'mls' },
    { team: 'Galaxy', league: 'MLS', api: 'mls' }
  ];

  // Use a free sports API service (placeholder URLs)
  const apiBaseUrls = {
    nba: 'https://site.api.espn.com/apis/site/v2/sports/basketball/nba/teams',
    mlb: 'https://site.api.espn.com/apis/site/v2/sports/baseball/mlb/teams',
    nfl: 'https://site.api.espn.com/apis/site/v2/sports/football/nfl/teams',
    mls: 'https://site.api.espn.com/apis/site/v2/sports/soccer/usa.1/teams'
  };

  const results = [];
  
  for (const team of laTeams.slice(0, 4)) { // Limit to 4 teams for demo
    try {
      // In production, you'd fetch real data here
      // For now, we'll create sample data
      results.push({
        team: team.team,
        league: team.league,
        status: 'Sample Data',
        score: 'Check official site',
        lastUpdate: new Date().toISOString()
      });
    } catch (error) {
      console.error(`Error fetching ${team.team} data:`, error);
    }
  }

  return results;
}

/**
 * Fetch MLB scores (placeholder)
 * @returns {Promise<Array>} MLB scores
 */
async function fetchMLBScores() {
  // Placeholder for MLB API integration
  return [
    {
      team: 'Dodgers',
      league: 'MLB',
      status: 'Next Game',
      score: 'Check schedule',
      lastUpdate: new Date().toISOString()
    }
  ];
}

/**
 * Fetch NBA scores (placeholder)
 * @returns {Promise<Array>} NBA scores
 */
async function fetchNBAScores() {
  // Placeholder for NBA API integration
  return [
    {
      team: 'Lakers',
      league: 'NBA',
      status: 'Season Update',
      score: 'Check official site',
      lastUpdate: new Date().toISOString()
    }
  ];
}

/**
 * Fetch NFL scores (placeholder)
 * @returns {Promise<Array>} NFL scores
 */
async function fetchNFLScores() {
  // Placeholder for NFL API integration
  return [
    {
      team: 'Rams',
      league: 'NFL',
      status: 'Season Update',
      score: 'Check schedule',
      lastUpdate: new Date().toISOString()
    }
  ];
}

/**
 * Display sports data in the grid
 * @param {HTMLElement} grid - Grid container
 * @param {Array} data - Sports data
 */
function displaySportsData(grid, data) {
  const html = data.map(item => `
    <div class="score-item ${getStatusClass(item.status)}">
      <div class="team-info">
        <span class="team-name">${item.team}</span>
        <span class="league-badge">${item.league}</span>
      </div>
      <div class="score-info">
        <span class="score">${item.score}</span>
        <span class="status">${item.status}</span>
      </div>
      <div class="update-time">
        Updated: ${formatTime(item.lastUpdate)}
      </div>
    </div>
  `).join('');

  grid.innerHTML = html;
}

/**
 * Display no data message
 * @param {HTMLElement} grid - Grid container
 */
function displayNoData(grid) {
  grid.innerHTML = `
    <div class="score-item no-data">
      <div class="no-data-content">
        <p><strong>🏈 No live games right now</strong></p>
        <p>Check back during game times for live updates!</p>
        <p><small>For the latest scores, visit official team websites</small></p>
      </div>
    </div>
  `;
}

/**
 * Display error message
 * @param {HTMLElement} grid - Grid container
 */
function displayError(grid) {
  grid.innerHTML = `
    <div class="score-item error">
      <div class="error-content">
        <p><strong>📱 Sports updates temporarily unavailable</strong></p>
        <p>Visit official team sites for the latest scores</p>
      </div>
    </div>
  `;
}

/**
 * Get CSS class based on game status
 * @param {string} status - Game status
 * @returns {string} CSS class
 */
function getStatusClass(status) {
  const statusLower = status.toLowerCase();
  if (statusLower.includes('live') || statusLower.includes('playing')) {
    return 'live';
  }
  if (statusLower.includes('final') || statusLower.includes('completed')) {
    return 'final';
  }
  if (statusLower.includes('upcoming') || statusLower.includes('scheduled')) {
    return 'upcoming';
  }
  return 'default';
}

/**
 * Format timestamp for display
 * @param {string} timestamp - ISO timestamp
 * @returns {string} Formatted time
 */
function formatTime(timestamp) {
  try {
    const date = new Date(timestamp);
    return date.toLocaleTimeString('en-US', {
      hour: 'numeric',
      minute: '2-digit',
      hour12: true
    });
  } catch (error) {
    return 'Unknown';
  }
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { initSportsLiveData };
}

// Auto-initialize if running in browser
if (typeof window !== 'undefined') {
  window.initSportsLiveData = initSportsLiveData;
}