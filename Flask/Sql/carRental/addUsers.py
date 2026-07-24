from database import DbManager
from config import DB_NAME, USER, PASSWORD, HOST

dbManager = DbManager(DB_NAME, USER, PASSWORD, HOST)
try:
    query = "CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;"

    dbManager.execute_query(query)

    query = """CREATE TABLE lyfter_car_rental.users(
    id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    user_name VARCHAR(30) UNIQUE NOT NULL,
    user_password VARCHAR(30) NOT NULL,
    born_date DATE NOT NULL,
    account_status VARCHAR(30) NOT NULL DEFAULT 'active'
    );"""

    dbManager.execute_query(query)

    query = """INSERT INTO lyfter_car_rental.users (full_name, email, user_name, user_password, birthday) 
    VALUES
('Jacquelynn Fay', 'jfay0@weather.com', 'jfay0', '927434728-6', '1980-11-29'),
('Abraham Iorizzo', 'aiorizzo1@npr.org', 'aiorizzo1', '922594782-8', '1991-04-24'),
('Kellina Kissock', 'kkissock2@google.com.hk', 'kkissock2', '200957043-X', '1985-03-30'),
('Quint Solan', 'qsolan3@wufoo.com', 'qsolan3', '331778025-8', '1982-08-25'),
('Nada Berth', 'nberth4@cdbaby.com', 'nberth4', '392134756-4', '1963-11-06'),
('Gallagher Bofield', 'gbofield5@omniture.com', 'gbofield5', '506419962-7', '1975-07-31'),
('Belicia Hagart', 'bhagart6@earthlink.net', 'bhagart6', '847023124-3', '1984-01-07'),
('Broderick Rabbage', 'brabbage7@state.tx.us', 'brabbage7', '797363889-X', '1974-07-23'),
('Hannie Hamley', 'hhamley8@state.gov', 'hhamley8', '536824696-X', '1984-11-15'),
('Jermaine Valois', 'jvalois9@google.com.au', 'jvalois9', '674793242-0', '1983-07-25'),
('Trista Akeherst', 'takehersta@seesaa.net', 'takehersta', '418871806-4', '1976-05-20'),
('Berkly Fawckner', 'bfawcknerb@blinklist.com', 'bfawcknerb', '044157069-0', '1987-01-26'),
('Glori Adderson', 'gaddersonc@bravesites.com', 'gaddersonc', '295059106-X', '1976-04-12'),
('Maxine Cleatherow', 'mcleatherowd@seattletimes.com', 'mcleatherowd', '140725222-4', '1975-04-18'),
('Valene Kilbourn', 'vkilbourne@marketwatch.com', 'vkilbourne', '160041372-2', '1972-12-28'),
('Seth Beastall', 'sbeastallf@angelfire.com', 'sbeastallf', '382039801-5', '1964-05-13'),
('Evvy Murrthum', 'emurrthumg@princeton.edu', 'emurrthumg', '574635535-6', '1973-07-29'),
('Quinton McCroft', 'qmccrofth@apple.com', 'qmccrofth', '752001132-1', '1972-03-28'),
('Jandy Dayer', 'jdayeri@twitpic.com', 'jdayeri', '153469310-6', '1973-04-25'),
('Ward Grindley', 'wgrindleyj@miibeian.gov.cn', 'wgrindleyj', '521774303-4', '1965-11-10'),
('Albrecht Fearby', 'afearbyk@dion.ne.jp', 'afearbyk', '277956515-2', '1978-08-14'),
('Dru Redmayne', 'dredmaynel@g.co', 'dredmaynel', '100855369-7', '1973-03-09'),
('Valdemar Temperton', 'vtempertonm@cam.ac.uk', 'vtempertonm', '663502843-9', '1963-03-28'),
('Emelda English', 'eenglishn@fc2.com', 'eenglishn', '531207787-9', '1986-01-23'),
('Rena Scarlon', 'rscarlono@addtoany.com', 'rscarlono', '683302576-2', '1973-03-03'),
('Woody Laven', 'wlavenp@edublogs.org', 'wlavenp', '008739056-6', '1975-03-12'),
('Aimee Dacombe', 'adacombeq@nytimes.com', 'adacombeq', '330457414-X', '1974-12-04'),
('Malvina Rainford', 'mrainfordr@wiley.com', 'mrainfordr', '992397010-8', '1969-08-26'),
('Gran Dudhill', 'gdudhills@seattletimes.com', 'gdudhills', '575283409-0', '1985-03-26'),
('Kelley Flory', 'kfloryt@businessinsider.com', 'kfloryt', '096810840-7', '1982-03-27'),
('Eleni Brandin', 'ebrandinu@nymag.com', 'ebrandinu', '698165617-5', '1964-03-19'),
('Mike Armstead', 'marmsteadv@flickr.com', 'marmsteadv', '722133392-0', '1984-06-19'),
('Maddi Ginity', 'mginityw@studiopress.com', 'mginityw', '303186939-7', '1984-01-01'),
('Clementius Hauxley', 'chauxleyx@abc.net.au', 'chauxleyx', '576738011-2', '1970-01-09'),
('Gae Sanham', 'gsanhamy@sohu.com', 'gsanhamy', '060165103-0', '1985-11-20'),
('Vina Aharoni', 'vaharoniz@hp.com', 'vaharoniz', '016556831-3', '1970-04-01'),
('Marley MacTeague', 'mmacteague10@about.me', 'mmacteague10', '216829286-8', '1992-03-04'),
('Lorain Carik', 'lcarik11@behance.net', 'lcarik11', '808601705-2', '1977-04-12'),
('Dun Firk', 'dfirk12@phpbb.com', 'dfirk12', '939500506-8', '1966-10-17'),
('Lidia Kenwyn', 'lkenwyn13@blog.com', 'lkenwyn13', '894379570-X', '1979-04-12'),
('Ferdinand Hupka', 'fhupka14@amazon.co.uk', 'fhupka14', '749504349-0', '1989-05-15'),
('Westley Crut', 'wcrut15@amazon.co.jp', 'wcrut15', '769439182-0', '1979-11-13'),
('Callie Linthead', 'clinthead16@phoca.cz', 'clinthead16', '733864325-3', '1990-04-08'),
('Deina Jessen', 'djessen17@arstechnica.com', 'djessen17', '080862768-6', '1976-02-12'),
('Frank Kebbell', 'fkebbell18@yahoo.co.jp', 'fkebbell18', '909222545-2', '1965-05-02'),
('Elbertine Neumann', 'eneumann19@mozilla.com', 'eneumann19', '465975172-4', '1976-09-26'),
('Miriam Moyce', 'mmoyce1a@gov.uk', 'mmoyce1a', '211701209-4', '1966-07-28'),
('Archy Iddenden', 'aiddenden1b@state.gov', 'aiddenden1b', '822922220-7', '1987-04-05'),
('Teresita Macklin', 'tmacklin1c@etsy.com', 'tmacklin1c', '167588216-9', '1985-01-22'),
('Mattheus Battram', 'mbattram1d@latimes.com', 'mbattram1d', '037706566-8', '1979-12-23'),
('Remy Birney', 'rbirney1e@yolasite.com', 'rbirney1e', '574526720-8', '1987-04-02'),
('Fayth Hatton', 'fhatton1f@unesco.org', 'fhatton1f', '587664043-3', '1964-05-02'),
('Carlin Cassin', 'ccassin1g@amazon.co.jp', 'ccassin1g', '407864813-4', '1989-06-25'),
('Laird Dungey', 'ldungey1h@sbwire.com', 'ldungey1h', '324568134-8', '1974-03-06'),
('Jill Dwire', 'jdwire1i@blogtalkradio.com', 'jdwire1i', '820264022-9', '1970-03-03'),
('Terry Hurley', 'thurley1j@engadget.com', 'thurley1j', '166561089-1', '1984-11-15'),
('Kinna Mapplethorpe', 'kmapplethorpe1k@unc.edu', 'kmapplethorpe1k', '272592153-8', '1977-09-03'),
('Maisey Chiommienti', 'mchiommienti1l@mapy.cz', 'mchiommienti1l', '232329186-6', '1985-04-03'),
('Trueman Normant', 'tnormant1m@mozilla.org', 'tnormant1m', '303538651-X', '1983-05-22'),
('Ingrim Ockwell', 'iockwell1n@is.gd', 'iockwell1n', '719168479-8', '1966-03-29'),
('Verine Dalman', 'vdalman1o@technorati.com', 'vdalman1o', '730571921-8', '1986-04-09'),
('Charley Hubbart', 'chubbart1p@ibm.com', 'chubbart1p', '497385985-0', '1984-03-27'),
('Drucill Klesl', 'dklesl1q@harvard.edu', 'dklesl1q', '175446769-5', '1978-05-07'),
('Bobinette Flaverty', 'bflaverty1r@oracle.com', 'bflaverty1r', '681204023-1', '1989-11-27'),
('Judah Truesdale', 'jtruesdale1s@youtu.be', 'jtruesdale1s', '425594800-3', '1985-09-16'),
('Dun Havard', 'dhavard1t@businesswire.com', 'dhavard1t', '991394464-3', '1991-07-23'),
('Cornelle Facher', 'cfacher1u@tumblr.com', 'cfacher1u', '830654792-6', '1969-06-12'),
('Reid Gobel', 'rgobel1v@4shared.com', 'rgobel1v', '660519075-0', '1972-04-03'),
('Broderick Canero', 'bcanero1w@mozilla.com', 'bcanero1w', '592547140-7', '1977-05-20'),
('Rhodia Klagges', 'rklagges1x@cisco.com', 'rklagges1x', '307413781-9', '1975-08-30'),
('Kendell Nottingam', 'knottingam1y@vkontakte.ru', 'knottingam1y', '654447131-3', '1975-05-06'),
('Vivie MacKeever', 'vmackeever1z@nytimes.com', 'vmackeever1z', '874949618-2', '1970-06-10'),
('Raimondo Bissiker', 'rbissiker20@geocities.jp', 'rbissiker20', '239243258-9', '1963-11-21'),
('Baily Bemlott', 'bbemlott21@ocn.ne.jp', 'bbemlott21', '811715362-9', '1992-03-29'),
('Oralie Sharrard', 'osharrard22@adobe.com', 'osharrard22', '974617161-5', '1967-12-03');"""
    dbManager.execute_query(query)
    print("Usuarios agregados satisfactoriamente")
except Exception as err:
    print("Error al inserta usuarios en la base de datos")
    print(err)
finally:
    dbManager.close_connection
