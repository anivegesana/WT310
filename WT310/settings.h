#ifndef __SETTINGS__
#define __SETTINGS__

#include <string>
#include <ctime>
using namespace std;

/* Power Meter Interfaces*/
extern const string K_inf_ethernet; 
extern const string K_inf_usb; 
/* Power Meter Modes*/
extern const string K_mode_dc; 
extern const string K_mode_rms; 



class pm_settings
{
	clock_t begin_time;			//Constructor generated time

public:
	string interface;			// USB, ETHERNET
	string ipaddress;			// XXX.XXX.XXX.XXX
	int log_duration;
	string mode;				// RMS, DC
	int data_update_interval;
	string csv_file;
	int initialize;
	int integrate;

	pm_settings();
	double elapsed_time();
	void parse_cmd_line(int argc, char **argv);
	void print_settings();
	void print_help();
};



#endif