import OOMP_projects
import OOMP_projects_BASE
import OOMP_projects_ADAF
import OOMP_projects_SPAR
import OOMP


OOMP.makePickle()
#OOMP.loadPickle()

#OOMP_projects.make()

#OOMP_projects.harvest()

#OOMP_projects.all()

#OOMP_projects_ADAF.farmProjects() ###### get repo list
#OOMP_projects_ADAF.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not
#OOMP_projects_ADAF.createProjects()

#OOMP_projects_SPAR.farmProjects() ###### get repo list
#OOMP_projects_SPAR.makeBaseProjects() #go through all repos and pull git details and whether they are a project or not
OOMP_projects_SPAR.createProjects()

#OOMP_projects_BASE.harvestProjects(easy=True) ###### the things that don't need a gui