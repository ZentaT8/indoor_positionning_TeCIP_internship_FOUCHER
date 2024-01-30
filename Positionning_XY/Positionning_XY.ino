#include <ADCInput.h>
#include <arduinoFFT.h>
#include <math.h>

#define NUM_POINTS 3
#define EPSILON 1e-9
#define MAX_ITERATIONS 1000

ADCInput adc(A0);
arduinoFFT FFT = arduinoFFT();

// Structure for representing the coordinates of a point
typedef struct {
    double x;
    double y;
} Point;

// Function for solving the system of equations
Point trilateration(Point* reference_points, double* distances) {
    int i;
    double A[NUM_POINTS - 1][2];
    double b[NUM_POINTS - 1];

    // Construction of the coordinate difference matrix
    for (i = 0; i < NUM_POINTS - 1; i++) {
        A[i][0] = 2 * (reference_points[i + 1].x - reference_points[0].x);
        A[i][1] = 2 * (reference_points[i + 1].y - reference_points[0].y);
    }

    // Construction of the distance squares vector
    for (i = 0; i < NUM_POINTS - 1; i++) {
        b[i] = pow(distances[0], 2) - pow(distances[i + 1], 2)
            - pow(reference_points[0].x, 2) + pow(reference_points[i + 1].x, 2)
            - pow(reference_points[0].y, 2) + pow(reference_points[i + 1].y, 2);
    }

    // Solving a system of linear equations
    double det = A[0][0] * A[1][1] - A[1][0] * A[0][1];
    if (det == 0) {
        // The system has no solution
        Point result = { NAN, NAN };
        return result;
    }

    double inv_det = 1 / det;
    double x = (A[1][1] * b[0] - A[0][1] * b[1]) * inv_det;
    double y = (A[0][0] * b[1] - A[1][0] * b[0]) * inv_det;

    Point result = { x, y };
    return result;
}

double equationL1(double x) {
    return -2 * pow(10, -14) * pow(x, 6) + 5 * pow(10, -21) * pow(x, 5) + 3 * pow(10, -9) * pow(x, 4) + 7 * pow(10, -16) * pow(x, 3) - 0.0005 * pow(x, 2) + 4 * pow(10, -11) * x + 27.791;
    //3 * pow(10, -9) * pow(x, 4) - 5 * pow(10, -18) * pow(x, 3) - 0.0005 * pow(x, 2) - 6 * pow(10, -13) * x + 27.802
    //return - 0.0005 * pow(x, 2) + 9 * pow(10, -16) * x + 27.115; old equation
}

double findXL1(double y) {
    double a = -220.0; // Minimum search value for x
    double b = 220.0; // Maximum search value for xM

    double mid, f_mid;

    for (int i = 0; i < MAX_ITERATIONS; i++) {
        mid = (a + b) / 2.0;
        f_mid = equationL1(mid);
        //Serial.printf("%lf\t%lf\t%lf\n", f_mid, y, mid);

        if (fabs(f_mid - y) < EPSILON) {
            return mid;
        }

        if (f_mid < y) {
            b = mid;
        } else {
            a = mid;
        }
    }

    // If convergence is not reached after the maximum number of iterations
    // or if no solution is found, return an invalid value
    return NAN;
}

double equationL2(double x) {
    return -2 * pow(10, -14) * pow(x, 6) - 1 * pow(10, -20) * pow(x, 5) + 7 * pow(10, -9) * pow(x, 4) + 9 * pow(10, -10) * pow(x, 3) - 0.00065 * pow(x, 2) + 8 * pow(10, -11) * x + 27.611;
    //6 * pow(10, -9) * pow(x, 4) + 15 * pow(10, -8) * pow(x, 3) - 0.00065 * pow(x, 2) - 3 * pow(10, -5) * x + 27.498  old equation
    //return - 0.0005 * pow(x, 2) + 9 * pow(10, -16) * x + 27.115; old equation
}

double findXL2(double y) {
    double a = -220.0; // Minimum search value for x
    double b = 220.0; // Maximum search value for xM

    double mid, f_mid;

    for (int i = 0; i < MAX_ITERATIONS; i++) {
        mid = (a + b) / 2.0;
        f_mid = equationL2(mid);
        //Serial.printf("%lf\t%lf\t%lf\n", f_mid, y, mid);

        if (fabs(f_mid - y) < EPSILON) {
            return mid;
        }

        if (f_mid < y) {
            b = mid;
        } else {
            a = mid;
        }
    }

    // If convergence is not reached after the maximum number of iterations
    // or if no solution is found, return an invalid value
    return NAN;
}

double equationL3(double x) {
    return -2 * pow(10, -14) * pow(x, 6) - 1 * pow(10, -20) * pow(x, 5) + 5 * pow(10, -9) * pow(x, 4) + 8 * pow(10, -16) * pow(x, 3) - 0.0005 * pow(x, 2) + 8 * pow(10, -11) * x + 31.174;
    //return - 0.0003 * pow(x, 2) + 1 * pow(10, -16) * x + 30.641; old equation
}

double findXL3(double y) {
    double a = -240.0; // Minimum search value for x
    double b = 240.0; // Maximum search value for x

    double mid, f_mid;

    for (int i = 0; i < MAX_ITERATIONS; i++) {
        mid = (a + b) / 2.0;
        f_mid = equationL3(mid);
        //Serial.printf("%lf\t%lf\t%lf\n", f_mid, y, mid);

        if (fabs(f_mid - y) < EPSILON) {
            return mid;
        }

        if (f_mid < y) {
            b = mid;
        } else {
            a = mid;
        }
    }

    // If convergence is not reached after the maximum number of iterations
    // or if no solution is found, return an invalid value
    return NAN;
}

void setup() {
  Serial.begin(115200);
  while(!Serial);

  const double samplingFrequency = 50000.0;
  const int numberOfSamples = 4096;
  const short nbAcqu = 10;
  const int frequency_1_lampe_1 = 2500, frequency_2_lampe_1 = 6000;
  const int frequency_1_lampe_2 = 4000, frequency_2_lampe_2 = 5500;
  const int frequency_1_lampe_3 = 1500, frequency_2_lampe_3 = 4600;
  int lamp1 = 0, lamp2 = 0;

  adc.begin();
  adc.setFrequency(samplingFrequency);

  // Definition of the variables for the FFT calculation
  double vReal[numberOfSamples];
  double vImg[numberOfSamples];
  float marge_erreur_freq = 50.0;
  float marge_erreur_amp = 2.0;
  
  float freq_max[10]; // Initialize an array to store the frequencies with max amplitude for each peak
  float amp_max[10]; // Initialize an array to store the max amplitudes for each peak

  // Initialize a 2D array to store the amplitudes and frequencies for each acquisition 
  float amps[numberOfSamples/2];
  float freqs[numberOfSamples/2];
  
  float marge_erreur = 70.0; // Set the margin of error to 70 Hz
  int index = -1;
  float max_amp = 0.0;
  int peak_count = 0; // Initialize a counter for the number of peaks found
  int t=0, cnt=0, t_mid=0;

  short minimized_surface = 0;
  short pourc_surf = 90;

  // Coordinates of known reference points
  Point reference_points[NUM_POINTS] = {
      { 85, 70 },  //lamp 1
      { 200, 70 }, //lamp 2
      { 140, 185 } //lamp 3
  };

  delay(1);
  int t_start;
  //int t_start=millis();
  
  while(1){
    //Reset variables
    memset(vReal, 0, sizeof(vReal)); // Reset
    memset(vImg, 0, sizeof(vImg)); // Reset
    memset(freqs, 0, sizeof(freqs)); // Reset
    memset(amps, 0, sizeof(amps)); // Reset
    memset(freq_max, 0, sizeof(freq_max)); // Reset
    memset(amp_max, 0, sizeof(amp_max)); // Reset
    peak_count = 0;
    index = -1;
    max_amp = 0.0;
    lamp1 = 0;
    lamp2 = 0;
    
    //Serial.printf("\t\tDébut du calcul\n");
    for (int j=0 ; j < nbAcqu ; j++) {
      //if (j==0)
        //Serial.printf("\tCalcul en cours ...\n", j+1);
      for (int i=0 ; i < numberOfSamples ; i++) {
        //Serial.printf("%d\n", adc.read());
        vReal[i]=(adc.read()*3.3)/4095;
        vImg[i]=0;
        //Serial.printf("%lf\n", vReal[i]);
      }

      //t_start = millis();
      /*The most time-consuming part of the programme*/
      FFT.Windowing(vReal, numberOfSamples, FFT_WIN_TYP_HAMMING, FFT_FORWARD);
      //Compute of the FFT
      FFT.Compute(vReal, vImg, numberOfSamples, FFT_FORWARD);
      //t_mid = millis();
      //Compute of the module of each values
      FFT.ComplexToMagnitude(vReal, vImg, numberOfSamples);
      /*_____________________________________________________*/

      //t = t_mid - t_start;
      //Serial.println(t);
      
      double delta_f = samplingFrequency / numberOfSamples;
      for (int i = 0; i < numberOfSamples/2; i++) {
        double temp = pow(vReal[i], 2);
        amps[i] = temp+amps[i];
        freqs[i] = i*delta_f;
        //Serial.printf("%.2f\n", amps[i]);
      }
    }
      
    //Serial.printf("\t\tFin du calcul\n");

    // Compute the average amplitudes for each frequency
    float avg_amps_db[numberOfSamples/2];
    memset(avg_amps_db, 0, sizeof(avg_amps_db));
    for (int i = 0; i < numberOfSamples/2; i++) {
      avg_amps_db[i] = 10*log10(amps[i]/nbAcqu);
      //Serial.printf("%.2f\n", amps[i]);
  
      //Serial.printf("%d,%.0f,%.2f\n", minimized_surface, freqs[i], avg_amps_db[i]);

      //Search peaks
      if (avg_amps_db[i] > 10) {
        if((freqs[i] >= frequency_1_lampe_1-marge_erreur_freq && freqs[i] <= frequency_1_lampe_1+marge_erreur_freq) || (freqs[i] >= frequency_2_lampe_1-marge_erreur_freq && freqs[i] <= frequency_2_lampe_1+marge_erreur_freq)
          || (freqs[i] >= frequency_1_lampe_2-marge_erreur_freq && freqs[i] <= frequency_1_lampe_2+marge_erreur_freq) || (freqs[i] >= frequency_2_lampe_2-marge_erreur_freq && freqs[i] <= frequency_2_lampe_2+marge_erreur_freq)
          || (freqs[i] >= frequency_1_lampe_3-marge_erreur_freq && freqs[i] <= frequency_1_lampe_3+marge_erreur_freq) || (freqs[i] >= frequency_2_lampe_3-marge_erreur_freq && freqs[i] <= frequency_2_lampe_3+marge_erreur_freq)){
//          if (freqs[i] >= 1000 && freqs[i] <= 8000){
            if (index == -1 || freqs[i] - freqs[index] > marge_erreur) {
              // New peak found
              index = i;
              max_amp = avg_amps_db[i];
              freq_max[peak_count] = freqs[i]; // Store the frequency with max amplitude for this peak
              amp_max[peak_count] = avg_amps_db[i]; // Store the max amplitude for this peak
              peak_count++; // Increment the peak counter
            } else if (avg_amps_db[i] > max_amp) {
              // New point with higher amplitude found for the same peak
              index = i;
              max_amp = avg_amps_db[i];
              freq_max[peak_count-1] = freqs[i]; // Update the frequency with max amplitude for this peak
              amp_max[peak_count-1] = avg_amps_db[i]; // Update the max amplitude for this peak
            }
        }
      }
    }

    //take the no-dB amplitude, to have more fluctuation
    float max_amps[10] = {0};
    for (int i = 0; i < peak_count; i++){
      max_amps[i] = pow(10, amp_max[i]/10);
    }

    // Print the frequencies and amplitudes with max amplitude for each peak
    for (int i = 0; i < peak_count; i++) {
      Serial.printf("Peak %d: Frequency : %0.0lf\tAmplitude db : %.2f\n", i+1, freq_max[i], amp_max[i]);
    }
    
    Serial.println();

    //Positionning
    if (peak_count < 2){
      Serial.printf("\n!!!!!!!!!!!!! Something is preventing the sensor from working properly !!!!!!!!!!!!!!!!!!!!!\n");
    }

    double Measured_Amp1 = (amp_max[1]+amp_max[5])/2;
    double Measured_Amp2 = (amp_max[2]+amp_max[4])/2;
    double Measured_Amp3 = (amp_max[0]+amp_max[3])/2;

    //Serial.printf("%.2lf;%.2lf;%.2lf\n", Measured_Amp1, Measured_Amp2, Measured_Amp3);

    double x1 = findXL1(Measured_Amp1);
    double x2 = findXL1(Measured_Amp2);
    double x3 = findXL3(Measured_Amp3);
    
    
    if (!isnan(x1)) {
        Serial.print("For y = ");
        Serial.print(Measured_Amp1);
        Serial.print(" dB, x is approximately equal to : ");
        Serial.print(x1);
        Serial.println(" cm");
    } else {
        Serial.print(Measured_Amp1);
        Serial.println("No solution found for x.");
        x1 = 0;
    }

    if (!isnan(x2)) {
        Serial.print("For y = ");
        Serial.print(Measured_Amp2);
        Serial.print(" dB, x is approximately equal to : ");
        Serial.print(x2);
        Serial.println(" cm");
    } else {
        Serial.print(Measured_Amp2);
        Serial.println("No solution found for x.");
        x2 = 0;
    }

    if (!isnan(x3)) {
        Serial.print("For y = ");
        Serial.print(Measured_Amp3);
        Serial.print(" dB, x is approximately equal to : ");
        Serial.print(x3);
        Serial.println(" cm");
    } else {
        Serial.println(Measured_Amp3);
        Serial.println("No solution found for x.");
    }
    
    // Distances measured from reference points
    double distances[NUM_POINTS] = { x1, x2, x3 };

    // Solving the system of equations
    Point coordinates = trilateration(reference_points, distances);

    // Displaying the coordinates of the estimated point
    if (isnan(coordinates.x) || isnan(coordinates.y)) {
        Serial.println("Impossible to determine the coordinates of the point.");
    }
    else {
        Serial.print("Estimated coordinates of the point : (");
        Serial.print(coordinates.x);
        Serial.print(", ");
        Serial.print(coordinates.y);
        //Serial.println();
        Serial.println(")");
    }

    Serial.printf("----------------------------------------------------------------------------\n");

    minimized_surface ++;
    pourc_surf += -45;

    //cnt++;
    //t = millis() - t_mid;
    //Serial.println(t);
    //delay(1000);
  }
  //Serial.println(t);
  //Serial.println(cnt);
}

void loop(){
  
}
