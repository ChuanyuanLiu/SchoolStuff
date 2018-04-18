import java.util.*;

class Identity {
	public final String name;
	public final int size;
	private List<Identity> association = new ArrayList<Identity>();
	
	// constructor
	public Identity(String name, int size) {
		this.name = name;
		this.size = size;
	}
	
	// toString
	@Override
	public String toString() {
		return this.name;
	}
	
	// getter and setter
	public List<Identity> getAssociation() {
		return association;
	}

	public void addAssociation(Identity a) {
		if (association.size() == size) return;
		association.add(a);
	}
}

class User extends Identity {
	// constructor
	public User(String name) {
		super(name, 10);
	}
}

class Group extends Identity {
	// constructor
	public Group(String name) {
		super(name, 100);
	}
	
	// toString
	@Override
	public String toString() {
		return name + this.getAssociation().toString();
	}
	
	// Question d
	public boolean alreadyMemeber(User user) {
		return getAssociation().contains(user);
	}
	
	// Question e
	public void addMember(User user) {
		if (alreadyMemeber(user)) return;
		this.addAssociation(user);
		user.addAssociation(this);
	}
	
	// Question f
	public void removeMemberByName(String name) {
		Identity tmp = null;
		for (Identity a: getAssociation()) {
			if (a.name == name) {
				tmp = a;
			}
		}
		getAssociation().remove(tmp);
	}
}

class Admin extends User {
	
	public Admin(String name) {
		super(name);
	}

	// toString
	@Override
	public String toString() {
		return name + " <admin>";
	}
}

public class Exam {
	
	public static void main(String[] args) {
		// question a
		User kevin = new User("Kevin");
		User bob = new User("Bob");
		System.out.println(kevin);
		
		// question b and e
		Group unimelb = new Group("Unimelb");
		unimelb.addMember(kevin);
		// test for double entries
		unimelb.addMember(kevin);
		System.out.println(unimelb);
		
		// question c
		Admin matt = new Admin("Matt");
		System.out.println(matt);
	
		
		// question d
		System.out.println(unimelb.alreadyMemeber(kevin));
		System.out.println(unimelb.alreadyMemeber(bob));

		// question f
		unimelb.removeMemberByName("Kevin");
		unimelb.removeMemberByName("Bob");
		System.out.println(unimelb);
	}
}
