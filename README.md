# **BioMeasure**  
Python scripts and shell scripts for **Raspbian** (should also work on Linux) to measure **Galvanic Skin Response (GSR)** using the **Seeed Grove hat + GSR sensor**.

---

## **Features**  
- **Real-Time GSR Monitoring** - Continuously monitor GSR values and display live plots using **Matplotlib**.  
- **CSV Data Logging** - Automatically logs GSR values along with timestamps into CSV files.  
- **Participant-Based File Management** - Data files are organised by participant numbers.  
- **Easy Hardware Integration** - Works seamlessly with **Seeed Grove hat** and **GSR sensors**.  

---

## **Installation**  

1. **Clone the Repository:**  
   ```bash
   git clone https://github.com/KarolynW/BioMeasure.git
   cd BioMeasure
   ```

2. **Install Dependencies:**  
   ```bash
   pip install matplotlib
   pip install seeed-python-adc  # For Grove sensor communication
   ```

3. **Setup Hardware:**  
   - Connect the **Grove GSR sensor** to the appropriate port.  
   - Ensure the **Seeed Grove hat** is properly attached to the Raspberry Pi.  

---

## **Usage**  

### **1. Start Measurement:**  
```bash
python bio_measure.py
```

- Enter the participant number when prompted.  
- The script automatically creates and manages CSV logs based on participant ID.  

### **2. Monitor Real-Time Data:**  
- Live plots show **GSR values** over time.  
- Graphs update dynamically during data collection.  

### **3. CSV Data Storage:**  
- All GSR data is saved in the `data/` folder in CSV format.  
- File names are based on participant IDs (e.g., `Participant_1_data.csv`).  

---

## **Code Overview**  

### **Main Script (bio_measure.py)**  
- Initializes the GSR sensor via **GroveGSRSensor** class.  
- Creates CSV logs and appends new data dynamically.  
- Uses **Matplotlib** for real-time data visualization.  

### **Sensor Class (grove_gsr_sensor.py)**  
- Handles communication with the **Grove ADC** module.  
- Reads raw GSR values from the sensor and provides them to the main script.  

---

## **Example Data Output (CSV):**  
| Timestamp           | GSR Value |
|---------------------|-----------|
| 2023-12-30 10:00:01 | 520       |
| 2023-12-30 10:00:02 | 515       |
| 2023-12-30 10:00:03 | 530       |

---

## **Notes:**  
- Adjust **ADC channel** if required (default is 0).  
- Sleep intervals (`time.sleep(0.3)`) can be modified for higher/lower frequency sampling.  

---

## **License**  
This project is licensed under the **MIT License**.

