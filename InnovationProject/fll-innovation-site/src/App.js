import './App.css'
import boulderImage from "./assets/boulder.png"
import demoUp from "./assets/demo_up.mp4"
import demoDown from "./assets/demo_down.mp4"
import { useState } from "react"

// --- STRUCTURED DATA FOR COLLAPSIBLE SECTIONS ---

// Data for the 'About Us' section
const aboutData = [
    { 
        title: "Our Mission", 
        detail: "The Boulder 4.0 and Artifact Armor were created to be a cost-effective and efficient solution to artifact transportation, which is currently a long, dangerous process." 
    },
    { 
        title: "Focus on Cost and Efficiency", 
        detail: "Our primary goal is to minimize both the time and budget required for artifact movement. By streamlining the transportation process, we free up critical resources for excavation, research, and conservation efforts." 
    },
    { 
        title: "Artifact Armor", 
        detail: "Artifact armor is a gyroscope that fits into pickup trucks. The artifact is placed on the gryoscope in order to keep the artifact level on rough terrain." 
    },
    { 
        title: "The Boulder 4.0", 
        detail: "The Boulder 4.0 is an all-in-one solution to the current problem of artifact transportation. With artifact armor built into the back of the truck, the Boulder 4.0 enhances artifact security, and is built specifically for rough terrain." 
    },

];

// Data for the 'The Transportation Problem' section
const mainProblemData = [
    { 
        title: "Current system for artifact transportation", 
        detail: "Despite being handled in a long, slow, process involving manual transportation and heavy lifting, artifacts are very prone to breaking. A famous example of this is king tut's chair. Despite taking several safety measures, the artifact was still damaged in the process." 
    },
    {
        title: "Consequences of This Method", 
        detail: "This method of transporting artifacts is not only a time-wasting process, but also wastes money. Heavy weights and excessive protective covering is used in this process, wasting money on resources that still end up damaging the artifacts in the end." 
    }
];

// Data for 'The Cost Crisis & Our $7,000 Solution' section
const fundingSolutionData = [
    {
        title: "A Fraction of the Cost", 
        detail: "Artifact Armor, our gyroscope, is priced at just $5,000, which is roughly a tenth the cost of the average specialized pickup truck trailer used for artifact transportation. This provides much-needed savings for archaeological projects." 
    },
    { 
        title: "Easily Fits Existing Trucks", 
        detail: "The Boulder 4.0 is designed for modularity, meaning it can be quickly and securely fitted into standard transportation vehicles, eliminating the high overhead cost of purchasing specialized transport fleets." 
    },
    { 
        title: "Artifacts Stay Level on Rough Terrain", 
        detail: "The internal mechanism actively swivels and adjusts instantaneously, ensuring the delicate payload remains perfectly level and isolated from bumps, dips, and high-frequency vibrations encountered on challenging terrain." 
    }
];

// Data for 'Our Product: Security and Efficiency' section
const productBenefitData = [
    { 
        title: "Faster Artifact Movement", 
        detail: "By significantly mitigating the risk of damage, we remove the need for excessively slow driving speeds and repeated stability checks, streamlining the overall timeline for moving artifacts from the dig site to the analysis lab." 
    },
    { 
        title: "Enhanced Public Accessibility", 
        detail: "A safer and faster transit process means artifacts spend less time in transit and storage, increasing the rate at which they can be prepared for study and display to the public." 
    },
    { 
        title: "Superior Protection and Safety", 
        detail: "The Boulder 4.0 offers guaranteed protection, drastically reducing the chance of chipping, cracking, or breaking, thereby preserving the integrity of invaluable historical items." 
    },
    { 
        title: "No Compromise on Safety Amidst Budget Cuts", 
        detail: "Our cost-effective solution ensures that archaeologists do not have to compromise on the safety of their finds, providing elite protection even as institutional and administrative funding faces further cuts." 
    }
];


// --- REUSABLE COLLAPSIBLE ITEM COMPONENT ---
const CollapsibleItem = ({ title, detail }) => {
    const [isOpen, setIsOpen] = useState(false);

    // Using inline styles for dropdown functionality, assuming a basic styling from app.css
    const itemStyle = {
        marginBottom: '10px',
        border: '1px solid #ccc',
        borderRadius: '8px',
        overflow: 'hidden',
        cursor: 'pointer',
        boxShadow: '0 2px 4px rgba(0,0,0,0.05)'
    };

    const headerStyle = {
        padding: '15px 20px',
        backgroundColor: '#3949ab', // Theme color
        color: 'white',
        fontWeight: 'bold',
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        transition: 'background-color 0.3s'
    };
    
    const contentStyle = {
        padding: '15px 20px',
        backgroundColor: '#f9f9ff',
        maxHeight: isOpen ? '500px' : '0',
        transition: 'max-height 0.4s ease-in-out, padding 0.4s ease-in-out',
        overflow: 'hidden',
        borderTop: isOpen ? '1px solid #ccc' : 'none'
    };

    return (
        <div style={itemStyle}>
            <div 
                style={headerStyle} 
                onClick={() => setIsOpen(!isOpen)}
            >
                {title}
                <span>{isOpen ? '▲' : '▼'}</span>
            </div>
            <div style={contentStyle}>
                <p>{detail}</p>
            </div>
        </div>
    );
};


// --- MAIN APP COMPONENT ---

function App() {

  const [currentVideo, setCurrentVideo] = useState(0);

  const videos = [demoUp, demoDown];

  const handleVideoEnd = () => {
    setCurrentVideo((prev) => (prev + 1) % videos.length);
  };

  return (
    <div className="App">
      <h1 className="title">Artifact Armor Inc.</h1>

      <div className ="about-us">
          <div className="about-us-content">
              <h2>About Us</h2>
              {aboutData.map((item, index) => (
                  <CollapsibleItem key={`about-${index}`} title={item.title} detail={item.detail} />
              ))}
          </div>
          <img src={boulderImage} alt="Artifact Armor Gyroscope"/>
      </div>
      <div className= "transportation_problem">
        <h2>The Transportation Problem</h2>
              {mainProblemData.map((item, index) => (
                  <CollapsibleItem key={`problem-${index}`} title={item.title} detail={item.detail} />
              ))}

              {/* The original image placeholder text */}
              <p>[Image of an artifact gyroscope being transported on a truck]</p>  
      </div>
        <div className="funding">
          <h2>The Cost Crisis & Our $7,000 Solution</h2>
              {fundingSolutionData.map((item, index) => (
                  <CollapsibleItem key={`funding-${index}`} title={item.title} detail={item.detail} />
              ))}
          <a>https://www.massarchaeology.org/support/donate/</a>
        </div>
      <div className="demo-video">
        <div className="demo-section">
       </div>
        <div className="demo-section-content">
          <h2>Our Product: Security and Efficiency</h2>
        {productBenefitData.map((item, index) => (
            <CollapsibleItem key={`product-${index}`} title={item.title} detail={item.detail} />
        ))}
        </div>  
         <div className="demo-section-video">
           <video
             key={currentVideo}
             src={videos[currentVideo]}
             muted
             autoPlay
             onEnded={handleVideoEnd}
            />
          </div>
      </div>
    </div>
  );
}

export default App;