# Table For Two

Table for Two is a web app that allows Mixpanelers the chance to meet with other Mixpanelers from different departments whenever they'd like. It prioritizes new hires, and allows lunch and coffee dates in 30 minute increments.

## Features
- Set your own availability
- Set your own profile settings (location? google hangout?)
- Matches folks automatically and puts the event on the calendar
- Sends out weekly email reminders


## TODOs

Signup
- [x] Create database and model
- [x] Create signup flow
- [x] Create index-logged-out page
- [x] Ask for extra information (edit-profile)
- [x] Create the form and edit-profile page
- [x] Save user in database
- [x] Create profile page
- [x] Show existing profile in form
- [ ] Test

Availability
- [x] Create index-logged-in page
- [x] Set availabilities in back-end
- [x] Show you made these availabilities
- [ ] Edit availabilities
- [ ] Remove availabilities
- [ ] Test

Matching
- [x] Match the people by availability and 1x/wk (frequency V2)
- [x] Show your future matches
- [x] Show your previous matches
- [x] Send a google calendar invite
- [x] Change everything to proper timezone
- [ ] Run the actual cron job
- [x] Test

Notifications
- [ ] Set notification based on frequency and current matchings

Mixpanel
- Goal: acquisition
- [ ] Alias/identify
- [ ] Signup flow (index -> signup -> profile -> save)
- [ ] Set availability
- [ ] Match made (server-side)
- [ ] Notification flow (notification sent -> set availability)
- [ ] People prop: email, dept, etc, number of matches, number of availabilities

Front-end
- PRETTIFY
- [ ] index-logged-out
- [ ] index-logged-in
- [ ] profile
- [ ] edit-profile


## Matching process
- For every availability, create an Availability for that user (date and time of beginning 1/2 hour, assuming timeslot is half hour)
- Runs a thing at 3pm the day before
- First pick are the newer Mixpanel hires
- Check for:
	- Only if fits their frequency of 1x/wk (V2 will be programmatic)
	- People who are available at the same time
	- Are in a different department
	- Haven't matched before
	- Those who are in the same location (last, GHangout)
- If that user is matched, then we'll set the name and email equal to the match


# V2
- BambooHR instead?
- Variable locations?
- See your Mixpanel calendar
- Programmatic frequencies
